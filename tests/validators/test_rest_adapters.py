"""
Tests for REST adapter module.
"""

import pytest
from unittest.mock import Mock, patch
import requests

from valuesets.validators.rest_adapters import (
    BaseRestAdapter,
    RORAdapter,
    get_rest_adapter
)


class TestBaseRestAdapter:
    """Tests for BaseRestAdapter base class."""

    def test_base_adapter_not_implemented(self):
        """Test that BaseRestAdapter.label() raises NotImplementedError."""
        adapter = BaseRestAdapter()
        with pytest.raises(NotImplementedError):
            adapter.label("TEST:123")


class TestRORAdapter:
    """Tests for RORAdapter implementation."""

    def test_extract_ror_id_from_curie(self):
        """Test extracting ROR ID from CURIE format."""
        adapter = RORAdapter()
        assert adapter._extract_ror_id("ROR:05gvnxz63") == "05gvnxz63"

    def test_extract_ror_id_from_url(self):
        """Test extracting ROR ID from URL format."""
        adapter = RORAdapter()
        assert adapter._extract_ror_id("https://ror.org/05gvnxz63") == "05gvnxz63"
        assert adapter._extract_ror_id("ror.org/05gvnxz63") == "05gvnxz63"

    def test_extract_ror_id_bare(self):
        """Test extracting ROR ID when already bare."""
        adapter = RORAdapter()
        assert adapter._extract_ror_id("05gvnxz63") == "05gvnxz63"

    def test_validate_ror_format_valid(self):
        """Test ROR ID format validation with valid IDs."""
        adapter = RORAdapter()
        # Valid ROR IDs
        assert adapter._validate_ror_format("05gvnxz63") is True
        assert adapter._validate_ror_format("01cwqze88") is True
        assert adapter._validate_ror_format("021nxhr62") is True

    def test_validate_ror_format_invalid(self):
        """Test ROR ID format validation with invalid IDs."""
        adapter = RORAdapter()
        # Invalid formats
        assert adapter._validate_ror_format("invalid") is False
        assert adapter._validate_ror_format("12345678") is False  # Doesn't start with 0
        assert adapter._validate_ror_format("0abcdefg1") is False  # Wrong length
        assert adapter._validate_ror_format("0abcdefgh") is False  # Wrong length
        assert adapter._validate_ror_format("") is False  # Empty

    def test_validate_ror_format_excludes_invalid_chars(self):
        """Test that ROR format validation excludes I, L, O, U per base32 Crockford."""
        adapter = RORAdapter()
        # These contain I, L, O, or U which are not valid in base32 Crockford
        assert adapter._validate_ror_format("0Iabcdef1") is False
        assert adapter._validate_ror_format("0Labcdef1") is False
        assert adapter._validate_ror_format("0Oabcdef1") is False
        assert adapter._validate_ror_format("0Uabcdef1") is False

    @patch('valuesets.validators.rest_adapters.requests.Session')
    def test_label_success(self, mock_session_class):
        """Test successful label retrieval from ROR API."""
        # Setup mock
        mock_session = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'status': 'active',
            'names': [
                {
                    'types': ['ror_display', 'label'],
                    'value': 'Argonne National Laboratory'
                }
            ]
        }
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        adapter = RORAdapter()
        label = adapter.label("ROR:05gvnxz63")

        assert label == "Argonne National Laboratory"
        mock_session.get.assert_called_once()

    @patch('valuesets.validators.rest_adapters.requests.Session')
    def test_label_not_found(self, mock_session_class):
        """Test label retrieval with 404 response."""
        mock_session = Mock()
        mock_response = Mock()
        mock_response.status_code = 404
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        adapter = RORAdapter()
        label = adapter.label("ROR:00000000")

        assert label is None

    @patch('valuesets.validators.rest_adapters.requests.Session')
    def test_label_invalid_format(self, mock_session_class):
        """Test that invalid format returns None without API call."""
        mock_session = Mock()
        mock_session_class.return_value = mock_session

        adapter = RORAdapter()
        label = adapter.label("INVALID")

        assert label is None
        # Should not make API call for invalid format
        mock_session.get.assert_not_called()

    @patch('valuesets.validators.rest_adapters.requests.Session')
    def test_label_inactive_organization(self, mock_session_class):
        """Test label retrieval for inactive organization."""
        mock_session = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'status': 'inactive',
            'names': [
                {
                    'types': ['ror_display'],
                    'value': 'Inactive Organization'
                }
            ]
        }
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        adapter = RORAdapter()
        label = adapter.label("ROR:01abc1234")

        # Should still return label even if inactive
        assert label == "Inactive Organization"

    @patch('valuesets.validators.rest_adapters.requests.Session')
    def test_label_fallback_to_first_name(self, mock_session_class):
        """Test fallback to first name if no ror_display."""
        mock_session = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'status': 'active',
            'names': [
                {
                    'types': ['label'],
                    'value': 'First Name'
                },
                {
                    'types': ['alias'],
                    'value': 'Alias Name'
                }
            ]
        }
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        adapter = RORAdapter()
        label = adapter.label("ROR:02def5678")

        assert label == "First Name"

    @patch('valuesets.validators.rest_adapters.requests.Session')
    def test_label_timeout_error(self, mock_session_class):
        """Test handling of timeout errors."""
        mock_session = Mock()
        mock_session.get.side_effect = requests.exceptions.Timeout()
        mock_session_class.return_value = mock_session

        adapter = RORAdapter()
        label = adapter.label("ROR:05gvnxz63")

        assert label is None

    @patch('valuesets.validators.rest_adapters.requests.Session')
    def test_label_request_exception(self, mock_session_class):
        """Test handling of general request exceptions."""
        mock_session = Mock()
        mock_session.get.side_effect = requests.exceptions.RequestException("Network error")
        mock_session_class.return_value = mock_session

        adapter = RORAdapter()
        label = adapter.label("ROR:05gvnxz63")

        assert label is None

    @patch('valuesets.validators.rest_adapters.requests.Session')
    def test_label_json_parse_error(self, mock_session_class):
        """Test handling of JSON parsing errors."""
        mock_session = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        adapter = RORAdapter()
        label = adapter.label("ROR:05gvnxz63")

        assert label is None

    @patch('valuesets.validators.rest_adapters.requests.Session')
    def test_label_malformed_response(self, mock_session_class):
        """Test handling of malformed API response."""
        mock_session = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'status': 'active'
            # Missing 'names' field
        }
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        adapter = RORAdapter()
        label = adapter.label("ROR:05gvnxz63")

        assert label is None

    @patch('valuesets.validators.rest_adapters.requests.Session')
    def test_label_empty_names(self, mock_session_class):
        """Test handling of empty names array."""
        mock_session = Mock()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'status': 'active',
            'names': []
        }
        mock_session.get.return_value = mock_response
        mock_session_class.return_value = mock_session

        adapter = RORAdapter()
        label = adapter.label("ROR:05gvnxz63")

        assert label is None

    def test_label_caching(self):
        """Test that LRU cache works correctly."""
        with patch('valuesets.validators.rest_adapters.requests.Session') as mock_session_class:
            mock_session = Mock()
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                'status': 'active',
                'names': [
                    {
                        'types': ['ror_display'],
                        'value': 'Test Organization'
                    }
                ]
            }
            mock_session.get.return_value = mock_response
            mock_session_class.return_value = mock_session

            adapter = RORAdapter()

            # First call
            label1 = adapter.label("ROR:05gvnxz63")
            # Second call should use cache
            label2 = adapter.label("ROR:05gvnxz63")

            assert label1 == "Test Organization"
            assert label2 == "Test Organization"
            # Should only call API once due to caching
            assert mock_session.get.call_count == 1

    def test_user_agent_header(self):
        """Test that User-Agent header is set correctly."""
        adapter = RORAdapter()
        assert 'User-Agent' in adapter._session.headers
        assert 'linkml-common-valuesets' in adapter._session.headers['User-Agent']


class TestRestAdapterFactory:
    """Tests for get_rest_adapter() factory function."""

    def test_get_rest_adapter_ror(self):
        """Test factory returns RORAdapter for rest:ror:."""
        adapter = get_rest_adapter("rest:ror:")
        assert isinstance(adapter, RORAdapter)

    def test_get_rest_adapter_unknown(self):
        """Test factory returns None for unknown adapter."""
        adapter = get_rest_adapter("rest:unknown:")
        assert adapter is None

    def test_get_rest_adapter_invalid_format(self):
        """Test factory returns None for invalid format."""
        adapter = get_rest_adapter("invalid")
        assert adapter is None

    def test_get_rest_adapter_empty(self):
        """Test factory returns None for empty string."""
        adapter = get_rest_adapter("")
        assert adapter is None

    def test_get_rest_adapter_none(self):
        """Test factory returns None for None input."""
        adapter = get_rest_adapter(None)
        assert adapter is None

    def test_get_rest_adapter_malformed(self):
        """Test factory handles malformed adapter strings."""
        adapter = get_rest_adapter("rest:")
        assert adapter is None

        adapter = get_rest_adapter("rest")
        assert adapter is None
