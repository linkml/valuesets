"""
Currency Value Sets

Value set of world currencies identified by their ISO 4217 three-letter alpha codes. Permissible value names are the ISO 4217 alpha-3 codes (an existing standard) rather than upper-snake-case. Covers monetary fields such as the PISCES Standard Flowsheet Format TEA_currency and per-mass price units. This is a curated set of actively circulating currencies and is extensible to the full ISO 4217 list.

Generated from: business/currencies.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class CurrencyCode(RichEnum):
    """
    World currencies by ISO 4217 alpha-3 code. The numeric_code, symbol, and minor_unit (number of decimal places) annotations record the corresponding ISO 4217 attributes.
    """
    # Enum members
    USD = "USD"
    EUR = "EUR"
    JPY = "JPY"
    GBP = "GBP"
    CNY = "CNY"
    AUD = "AUD"
    CAD = "CAD"
    CHF = "CHF"
    HKD = "HKD"
    SGD = "SGD"
    SEK = "SEK"
    NOK = "NOK"
    DKK = "DKK"
    NZD = "NZD"
    KRW = "KRW"
    INR = "INR"
    BRL = "BRL"
    ZAR = "ZAR"
    RUB = "RUB"
    MXN = "MXN"
    TRY = "TRY"
    PLN = "PLN"
    THB = "THB"
    IDR = "IDR"
    MYR = "MYR"
    PHP = "PHP"
    AED = "AED"
    SAR = "SAR"
    ILS = "ILS"
    CZK = "CZK"
    HUF = "HUF"
    RON = "RON"
    UAH = "UAH"
    CLP = "CLP"
    COP = "COP"
    ARS = "ARS"
    EGP = "EGP"
    NGN = "NGN"
    KES = "KES"
    PKR = "PKR"
    BDT = "BDT"
    VND = "VND"
    TWD = "TWD"
    KWD = "KWD"
    BHD = "BHD"
    OMR = "OMR"
    QAR = "QAR"
    ISK = "ISK"

# Set metadata after class creation
CurrencyCode._metadata = {
    "USD": {'description': 'United States dollar', 'annotations': {'numeric_code': '840', 'symbol': '$', 'minor_unit': 2}},
    "EUR": {'description': 'Euro', 'annotations': {'numeric_code': '978', 'symbol': '€', 'minor_unit': 2}},
    "JPY": {'description': 'Japanese yen', 'annotations': {'numeric_code': '392', 'symbol': '¥', 'minor_unit': 0}},
    "GBP": {'description': 'British pound sterling', 'annotations': {'numeric_code': '826', 'symbol': '£', 'minor_unit': 2}},
    "CNY": {'description': 'Chinese yuan renminbi', 'annotations': {'numeric_code': '156', 'symbol': '¥', 'minor_unit': 2}},
    "AUD": {'description': 'Australian dollar', 'annotations': {'numeric_code': '036', 'symbol': '$', 'minor_unit': 2}},
    "CAD": {'description': 'Canadian dollar', 'annotations': {'numeric_code': '124', 'symbol': '$', 'minor_unit': 2}},
    "CHF": {'description': 'Swiss franc', 'annotations': {'numeric_code': '756', 'symbol': 'Fr', 'minor_unit': 2}},
    "HKD": {'description': 'Hong Kong dollar', 'annotations': {'numeric_code': '344', 'symbol': '$', 'minor_unit': 2}},
    "SGD": {'description': 'Singapore dollar', 'annotations': {'numeric_code': '702', 'symbol': '$', 'minor_unit': 2}},
    "SEK": {'description': 'Swedish krona', 'annotations': {'numeric_code': '752', 'symbol': 'kr', 'minor_unit': 2}},
    "NOK": {'description': 'Norwegian krone', 'annotations': {'numeric_code': '578', 'symbol': 'kr', 'minor_unit': 2}},
    "DKK": {'description': 'Danish krone', 'annotations': {'numeric_code': '208', 'symbol': 'kr', 'minor_unit': 2}},
    "NZD": {'description': 'New Zealand dollar', 'annotations': {'numeric_code': '554', 'symbol': '$', 'minor_unit': 2}},
    "KRW": {'description': 'South Korean won', 'annotations': {'numeric_code': '410', 'symbol': '₩', 'minor_unit': 0}},
    "INR": {'description': 'Indian rupee', 'annotations': {'numeric_code': '356', 'symbol': '₹', 'minor_unit': 2}},
    "BRL": {'description': 'Brazilian real', 'annotations': {'numeric_code': '986', 'symbol': 'R$', 'minor_unit': 2}},
    "ZAR": {'description': 'South African rand', 'annotations': {'numeric_code': '710', 'symbol': 'R', 'minor_unit': 2}},
    "RUB": {'description': 'Russian ruble', 'annotations': {'numeric_code': '643', 'symbol': '₽', 'minor_unit': 2}},
    "MXN": {'description': 'Mexican peso', 'annotations': {'numeric_code': '484', 'symbol': '$', 'minor_unit': 2}},
    "TRY": {'description': 'Turkish lira', 'annotations': {'numeric_code': '949', 'symbol': '₺', 'minor_unit': 2}},
    "PLN": {'description': 'Polish zloty', 'annotations': {'numeric_code': '985', 'symbol': 'zł', 'minor_unit': 2}},
    "THB": {'description': 'Thai baht', 'annotations': {'numeric_code': '764', 'symbol': '฿', 'minor_unit': 2}},
    "IDR": {'description': 'Indonesian rupiah', 'annotations': {'numeric_code': '360', 'symbol': 'Rp', 'minor_unit': 2}},
    "MYR": {'description': 'Malaysian ringgit', 'annotations': {'numeric_code': '458', 'symbol': 'RM', 'minor_unit': 2}},
    "PHP": {'description': 'Philippine peso', 'annotations': {'numeric_code': '608', 'symbol': '₱', 'minor_unit': 2}},
    "AED": {'description': 'United Arab Emirates dirham', 'annotations': {'numeric_code': '784', 'minor_unit': 2}},
    "SAR": {'description': 'Saudi riyal', 'annotations': {'numeric_code': '682', 'minor_unit': 2}},
    "ILS": {'description': 'Israeli new shekel', 'annotations': {'numeric_code': '376', 'symbol': '₪', 'minor_unit': 2}},
    "CZK": {'description': 'Czech koruna', 'annotations': {'numeric_code': '203', 'symbol': 'Kč', 'minor_unit': 2}},
    "HUF": {'description': 'Hungarian forint', 'annotations': {'numeric_code': '348', 'symbol': 'Ft', 'minor_unit': 2}},
    "RON": {'description': 'Romanian leu', 'annotations': {'numeric_code': '946', 'symbol': 'lei', 'minor_unit': 2}},
    "UAH": {'description': 'Ukrainian hryvnia', 'annotations': {'numeric_code': '980', 'symbol': '₴', 'minor_unit': 2}},
    "CLP": {'description': 'Chilean peso', 'annotations': {'numeric_code': '152', 'symbol': '$', 'minor_unit': 0}},
    "COP": {'description': 'Colombian peso', 'annotations': {'numeric_code': '170', 'symbol': '$', 'minor_unit': 2}},
    "ARS": {'description': 'Argentine peso', 'annotations': {'numeric_code': '032', 'symbol': '$', 'minor_unit': 2}},
    "EGP": {'description': 'Egyptian pound', 'annotations': {'numeric_code': '818', 'symbol': '£', 'minor_unit': 2}},
    "NGN": {'description': 'Nigerian naira', 'annotations': {'numeric_code': '566', 'symbol': '₦', 'minor_unit': 2}},
    "KES": {'description': 'Kenyan shilling', 'annotations': {'numeric_code': '404', 'symbol': 'Sh', 'minor_unit': 2}},
    "PKR": {'description': 'Pakistani rupee', 'annotations': {'numeric_code': '586', 'symbol': '₨', 'minor_unit': 2}},
    "BDT": {'description': 'Bangladeshi taka', 'annotations': {'numeric_code': '050', 'symbol': '৳', 'minor_unit': 2}},
    "VND": {'description': 'Vietnamese dong', 'annotations': {'numeric_code': '704', 'symbol': '₫', 'minor_unit': 0}},
    "TWD": {'description': 'New Taiwan dollar', 'annotations': {'numeric_code': '901', 'symbol': '$', 'minor_unit': 2}},
    "KWD": {'description': 'Kuwaiti dinar', 'annotations': {'numeric_code': '414', 'minor_unit': 3}},
    "BHD": {'description': 'Bahraini dinar', 'annotations': {'numeric_code': '048', 'minor_unit': 3}},
    "OMR": {'description': 'Omani rial', 'annotations': {'numeric_code': '512', 'minor_unit': 3}},
    "QAR": {'description': 'Qatari riyal', 'annotations': {'numeric_code': '634', 'minor_unit': 2}},
    "ISK": {'description': 'Icelandic krona', 'annotations': {'numeric_code': '352', 'symbol': 'kr', 'minor_unit': 0}},
}

__all__ = [
    "CurrencyCode",
]