"""
Fixity and Integrity Verification

Value sets for data integrity verification, including cryptographic
hash functions and fixity-related metadata. Based on PREMIS 3.0.

Fixity information is used to verify that a digital object has not
been altered in an undocumented manner.

See: https://www.loc.gov/standards/premis/


Generated from: preservation/fixity.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class CryptographicHashFunction(RichEnum):
    """
    Algorithms that take an input and return a fixed-size string (hash value).
    Used for verifying data integrity and creating digital signatures.
    Based on PREMIS cryptographic hash functions vocabulary.
    
    """
    # Enum members
    ADLER_32 = "ADLER_32"
    CRC32 = "CRC32"
    HAVAL = "HAVAL"
    MD2 = "MD2"
    MD4 = "MD4"
    MD5 = "MD5"
    MD6 = "MD6"
    SHA_1 = "SHA_1"
    SHA_224 = "SHA_224"
    SHA_256 = "SHA_256"
    SHA_384 = "SHA_384"
    SHA_512 = "SHA_512"
    SHA3_224 = "SHA3_224"
    SHA3_256 = "SHA3_256"
    SHA3_384 = "SHA3_384"
    SHA3_512 = "SHA3_512"
    BLAKE2B_256 = "BLAKE2B_256"
    BLAKE2B_384 = "BLAKE2B_384"
    BLAKE2B_512 = "BLAKE2B_512"
    BLAKE3 = "BLAKE3"
    TIGER = "TIGER"
    WHIRLPOOL = "WHIRLPOOL"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
CryptographicHashFunction._metadata = {
    "ADLER_32": {'description': 'A checksum algorithm developed by Mark Adler. Faster than CRC32\nbut with weaker error detection. Used in zlib compression.\n', 'meaning': 'premis:cryptographicHashFunctions/adl', 'annotations': {'output_bits': 32, 'security_level': 'non-cryptographic'}},
    "CRC32": {'description': 'Cyclic Redundancy Check with 32-bit output. Used for error detection\nin network transmissions and storage. Not cryptographically secure.\n', 'meaning': 'premis:cryptographicHashFunctions/crc', 'annotations': {'output_bits': 32, 'security_level': 'non-cryptographic'}},
    "HAVAL": {'description': 'A cryptographic hash function that can produce hash values of\n128, 160, 192, 224, or 256 bits. Variable number of rounds.\n', 'meaning': 'premis:cryptographicHashFunctions/hav', 'annotations': {'output_bits': 'variable', 'security_level': 'deprecated'}},
    "MD2": {'description': 'Message Digest 2 algorithm producing a 128-bit hash value.\nDesigned for 8-bit computers. Considered cryptographically broken.\n', 'meaning': 'premis:cryptographicHashFunctions/md2', 'annotations': {'output_bits': 128, 'security_level': 'broken'}},
    "MD4": {'description': 'Message Digest 4 algorithm producing a 128-bit hash value.\nPredecessor to MD5. Considered cryptographically broken.\n', 'annotations': {'output_bits': 128, 'security_level': 'broken'}},
    "MD5": {'description': 'Message Digest 5 algorithm producing a 128-bit hash value.\nWidely used but vulnerable to collision attacks. Acceptable\nfor non-security integrity checks only.\n', 'meaning': 'premis:cryptographicHashFunctions/md5', 'annotations': {'output_bits': 128, 'security_level': 'weak'}},
    "MD6": {'description': 'Message Digest 6 algorithm with variable output size.\nDesigned as a candidate for SHA-3 but not selected.\n', 'annotations': {'output_bits': 'variable', 'security_level': 'adequate'}},
    "SHA_1": {'description': 'Secure Hash Algorithm 1 producing a 160-bit hash value.\nDeprecated for security applications due to collision vulnerabilities.\nStill acceptable for integrity verification in some contexts.\n', 'meaning': 'premis:cryptographicHashFunctions/sha1', 'annotations': {'output_bits': 160, 'security_level': 'weak'}, 'aliases': ['SHA1']},
    "SHA_224": {'description': 'SHA-2 variant producing a 224-bit hash value.\nTruncated version of SHA-256.\n', 'annotations': {'output_bits': 224, 'security_level': 'secure'}, 'aliases': ['SHA224']},
    "SHA_256": {'description': 'SHA-2 variant producing a 256-bit hash value.\nWidely used and considered secure for most applications.\nRecommended for digital preservation.\n', 'meaning': 'premis:cryptographicHashFunctions/sha256', 'annotations': {'output_bits': 256, 'security_level': 'secure'}, 'aliases': ['SHA256']},
    "SHA_384": {'description': 'SHA-2 variant producing a 384-bit hash value.\nTruncated version of SHA-512.\n', 'meaning': 'premis:cryptographicHashFunctions/sha384', 'annotations': {'output_bits': 384, 'security_level': 'secure'}, 'aliases': ['SHA384']},
    "SHA_512": {'description': 'SHA-2 variant producing a 512-bit hash value.\nHighest security level in the SHA-2 family.\n', 'meaning': 'premis:cryptographicHashFunctions/sha512', 'annotations': {'output_bits': 512, 'security_level': 'secure'}, 'aliases': ['SHA512']},
    "SHA3_224": {'description': 'SHA-3 variant producing a 224-bit hash value.\nBased on the Keccak algorithm.\n', 'annotations': {'output_bits': 224, 'security_level': 'secure'}},
    "SHA3_256": {'description': 'SHA-3 variant producing a 256-bit hash value.\nBased on the Keccak algorithm. Provides defense against\nlength extension attacks.\n', 'annotations': {'output_bits': 256, 'security_level': 'secure'}},
    "SHA3_384": {'description': 'SHA-3 variant producing a 384-bit hash value.\nBased on the Keccak algorithm.\n', 'annotations': {'output_bits': 384, 'security_level': 'secure'}},
    "SHA3_512": {'description': 'SHA-3 variant producing a 512-bit hash value.\nBased on the Keccak algorithm.\n', 'annotations': {'output_bits': 512, 'security_level': 'secure'}},
    "BLAKE2B_256": {'description': 'BLAKE2b variant producing a 256-bit hash value.\nFaster than MD5 and SHA-1 while being more secure.\n', 'annotations': {'output_bits': 256, 'security_level': 'secure'}},
    "BLAKE2B_384": {'description': 'BLAKE2b variant producing a 384-bit hash value.\n', 'annotations': {'output_bits': 384, 'security_level': 'secure'}},
    "BLAKE2B_512": {'description': 'BLAKE2b variant producing a 512-bit hash value.\nOptimized for 64-bit platforms.\n', 'annotations': {'output_bits': 512, 'security_level': 'secure'}},
    "BLAKE3": {'description': 'Latest BLAKE variant, extremely fast with 256-bit output.\nSupports parallelization and incremental hashing.\n', 'annotations': {'output_bits': 256, 'security_level': 'secure'}},
    "TIGER": {'description': 'A cryptographic hash function designed for 64-bit platforms.\nProduces a 192-bit hash value.\n', 'meaning': 'premis:cryptographicHashFunctions/tig', 'annotations': {'output_bits': 192, 'security_level': 'adequate'}},
    "WHIRLPOOL": {'description': 'A cryptographic hash function producing a 512-bit hash value.\nBased on a modified AES block cipher.\n', 'meaning': 'premis:cryptographicHashFunctions/whi', 'annotations': {'output_bits': 512, 'security_level': 'secure'}},
    "UNKNOWN": {'description': 'The hash algorithm is not known or not specified.', 'meaning': 'premis:cryptographicHashFunctions/unk'},
}

__all__ = [
    "CryptographicHashFunction",
]