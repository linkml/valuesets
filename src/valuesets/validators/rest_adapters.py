"""
REST API adapters for ontology validation.

This module provides adapter classes that implement the OAK interface
for REST APIs that are not supported by OAK directly. This allows
seamless integration into the existing validation framework.
"""

import logging
import re
import requests
from typing import Optional
from functools import lru_cache

logger = logging.getLogger(__name__)


class BaseRestAdapter:
    """
    Base class for REST API adapters.

    Implements the minimal OAK interface needed for validation:
    - label(curie) -> Optional[str]
    """

    def label(self, curie: str) -> Optional[str]:
        """
        Get the label for a term.

        Args:
            curie: CURIE identifier (e.g., "ROR:041nk4h53")

        Returns:
            Label string or None if not found
        """
        raise NotImplementedError("Subclasses must implement label()")


class RORAdapter(BaseRestAdapter):
    """
    Adapter for Research Organization Registry (ROR) API.

    ROR provides persistent identifiers for research organizations.
    API: https://api.ror.org/v2/organizations
    Docs: https://ror.readme.io/docs/rest-api

    Example:
        >>> adapter = RORAdapter()
        >>> adapter.label("ROR:041nk4h53")
        'Lawrence Livermore National Laboratory'

        # Also accepts full URLs
        >>> adapter.label("https://ror.org/041nk4h53")
        'Lawrence Livermore National Laboratory'
    """

    # Regex for ROR ID validation (base32 Crockford, excludes I,L,O,U)
    ROR_PATTERN = re.compile(r'^0[a-hj-km-np-tv-z|0-9]{6}[0-9]{2}$')

    def __init__(self, api_base: str = "https://api.ror.org/v2/organizations"):
        """
        Initialize the ROR adapter.

        Args:
            api_base: Base URL for ROR API (default: v2 endpoint)
        """
        self.api_base = api_base
        self._session = requests.Session()
        self._session.headers.update({
            'User-Agent': 'linkml-common-valuesets/1.0 (https://github.com/linkml/common-value-sets)'
        })

    def _extract_ror_id(self, curie: str) -> str:
        """
        Extract ROR ID from CURIE or URL.

        Args:
            curie: ROR identifier (ROR:041nk4h53, ror.org/041nk4h53, or https://ror.org/041nk4h53)

        Returns:
            9-character ROR ID (e.g., "041nk4h53")
        """
        # Handle CURIE format (ROR:041nk4h53)
        if curie.startswith("ROR:"):
            return curie[4:]

        # Handle URL formats
        if "ror.org/" in curie:
            return curie.split("ror.org/")[-1]

        # Already just the ID
        return curie

    def _validate_ror_format(self, ror_id: str) -> bool:
        """
        Validate ROR ID format.

        Args:
            ror_id: 9-character ROR ID

        Returns:
            True if format is valid
        """
        return bool(self.ROR_PATTERN.match(ror_id))

    @lru_cache(maxsize=1000)
    def label(self, curie: str) -> Optional[str]:
        """
        Get the display name for a ROR organization.

        Args:
            curie: ROR identifier in any accepted format

        Returns:
            Official display name from ROR, or None if not found
        """
        ror_id = self._extract_ror_id(curie)

        # Quick format validation
        if not self._validate_ror_format(ror_id):
            logger.warning(f"Invalid ROR ID format: {ror_id}")
            return None

        # Query ROR API
        try:
            url = f"{self.api_base}/{ror_id}"
            response = self._session.get(url, timeout=10)

            if response.status_code == 404:
                logger.debug(f"ROR ID not found: {ror_id}")
                return None

            if response.status_code != 200:
                logger.warning(f"ROR API returned status {response.status_code} for {ror_id}")
                return None

            data = response.json()

            # Check if active (optional - could make this configurable)
            if data.get('status') != 'active':
                logger.info(f"ROR ID {ror_id} has status: {data.get('status')}")

            # Extract display name from names array
            # Look for name with type "ror_display"
            names = data.get('names', [])
            for name_obj in names:
                if 'ror_display' in name_obj.get('types', []):
                    return name_obj.get('value')

            # Fallback: return first name if no ror_display found
            if names:
                return names[0].get('value')

            logger.warning(f"No name found in ROR record for {ror_id}")
            return None

        except requests.exceptions.Timeout:
            logger.warning(f"Timeout querying ROR API for {ror_id}")
            return None
        except requests.exceptions.RequestException as e:
            logger.warning(f"Error querying ROR API for {ror_id}: {e}")
            return None
        except (ValueError, KeyError) as e:
            logger.warning(f"Error parsing ROR API response for {ror_id}: {e}")
            return None


def get_rest_adapter(adapter_string: str) -> Optional[BaseRestAdapter]:
    """
    Factory function to create REST adapters based on adapter string.

    This allows oak_config.yaml to specify REST adapters using a
    special syntax like "rest:ror:" or "rest:api_name:".

    Args:
        adapter_string: Adapter specification (e.g., "rest:ror:")

    Returns:
        Appropriate REST adapter instance, or None if not recognized

    Example:
        In oak_config.yaml:
            ROR: rest:ror:

        Then in enum_evaluator.py:
            adapter = get_rest_adapter("rest:ror:")
            label = adapter.label("ROR:041nk4h53")
    """
    if not adapter_string or not adapter_string.startswith("rest:"):
        return None

    # Parse rest:api_name: format
    parts = adapter_string.split(":")
    if len(parts) < 2:
        logger.warning(f"Invalid REST adapter string: {adapter_string}")
        return None

    api_name = parts[1].lower()

    # Map to adapter classes
    adapters = {
        'ror': RORAdapter,
        # Future: 'wikidata': WikidataAdapter, etc.
    }

    adapter_class = adapters.get(api_name)
    if not adapter_class:
        logger.warning(f"Unknown REST API adapter: {api_name}")
        return None

    try:
        return adapter_class()
    except Exception as e:
        logger.warning(f"Error creating {api_name} adapter: {e}")
        return None
