"""
Temporal and Time-Related Value Sets

Value sets for temporal concepts including days, months, time periods, and durations

Generated from: time/temporal.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class DayOfWeek(RichEnum):
    """
    Days of the week following ISO 8601 standard (Monday = 1)
    """
    # Enum members
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"

# Set metadata after class creation
DayOfWeek._metadata = {
    "MONDAY": {'description': 'Monday (first day of week in ISO 8601)', 'meaning': 'TIME:Monday', 'annotations': {'iso_number': 1, 'abbreviation': 'Mon'}},
    "TUESDAY": {'description': 'Tuesday', 'meaning': 'TIME:Tuesday', 'annotations': {'iso_number': 2, 'abbreviation': 'Tue'}},
    "WEDNESDAY": {'description': 'Wednesday', 'meaning': 'TIME:Wednesday', 'annotations': {'iso_number': 3, 'abbreviation': 'Wed'}},
    "THURSDAY": {'description': 'Thursday', 'meaning': 'TIME:Thursday', 'annotations': {'iso_number': 4, 'abbreviation': 'Thu'}},
    "FRIDAY": {'description': 'Friday', 'meaning': 'TIME:Friday', 'annotations': {'iso_number': 5, 'abbreviation': 'Fri'}},
    "SATURDAY": {'description': 'Saturday', 'meaning': 'TIME:Saturday', 'annotations': {'iso_number': 6, 'abbreviation': 'Sat'}},
    "SUNDAY": {'description': 'Sunday (last day of week in ISO 8601)', 'meaning': 'TIME:Sunday', 'annotations': {'iso_number': 7, 'abbreviation': 'Sun'}},
}

class Month(RichEnum):
    """
    Months of the year
    """
    # Enum members
    JANUARY = "JANUARY"
    FEBRUARY = "FEBRUARY"
    MARCH = "MARCH"
    APRIL = "APRIL"
    MAY = "MAY"
    JUNE = "JUNE"
    JULY = "JULY"
    AUGUST = "AUGUST"
    SEPTEMBER = "SEPTEMBER"
    OCTOBER = "OCTOBER"
    NOVEMBER = "NOVEMBER"
    DECEMBER = "DECEMBER"

# Set metadata after class creation
Month._metadata = {
    "JANUARY": {'description': 'January', 'meaning': 'greg:January', 'rank': 1, 'annotations': {'abbreviation': 'Jan', 'days': 31}},
    "FEBRUARY": {'description': 'February', 'meaning': 'greg:February', 'rank': 2, 'annotations': {'abbreviation': 'Feb', 'days': '28/29'}},
    "MARCH": {'description': 'March', 'meaning': 'greg:March', 'rank': 3, 'annotations': {'abbreviation': 'Mar', 'days': 31}},
    "APRIL": {'description': 'April', 'meaning': 'greg:April', 'rank': 4, 'annotations': {'abbreviation': 'Apr', 'days': 30}},
    "MAY": {'description': 'May', 'meaning': 'greg:May', 'rank': 5, 'annotations': {'abbreviation': 'May', 'days': 31}},
    "JUNE": {'description': 'June', 'meaning': 'greg:June', 'rank': 6, 'annotations': {'abbreviation': 'Jun', 'days': 30}},
    "JULY": {'description': 'July', 'meaning': 'greg:July', 'rank': 7, 'annotations': {'abbreviation': 'Jul', 'days': 31}},
    "AUGUST": {'description': 'August', 'meaning': 'greg:August', 'rank': 8, 'annotations': {'abbreviation': 'Aug', 'days': 31}},
    "SEPTEMBER": {'description': 'September', 'meaning': 'greg:September', 'rank': 9, 'annotations': {'abbreviation': 'Sep', 'days': 30}},
    "OCTOBER": {'description': 'October', 'meaning': 'greg:October', 'rank': 10, 'annotations': {'abbreviation': 'Oct', 'days': 31}},
    "NOVEMBER": {'description': 'November', 'meaning': 'greg:November', 'rank': 11, 'annotations': {'abbreviation': 'Nov', 'days': 30}},
    "DECEMBER": {'description': 'December', 'meaning': 'greg:December', 'rank': 12, 'annotations': {'abbreviation': 'Dec', 'days': 31}},
}

class Quarter(RichEnum):
    """
    Calendar quarters
    """
    # Enum members
    Q1 = "Q1"
    Q2 = "Q2"
    Q3 = "Q3"
    Q4 = "Q4"

# Set metadata after class creation
Quarter._metadata = {
    "Q1": {'description': 'First quarter (January-March)', 'annotations': {'months': 'Jan-Mar'}},
    "Q2": {'description': 'Second quarter (April-June)', 'annotations': {'months': 'Apr-Jun'}},
    "Q3": {'description': 'Third quarter (July-September)', 'annotations': {'months': 'Jul-Sep'}},
    "Q4": {'description': 'Fourth quarter (October-December)', 'annotations': {'months': 'Oct-Dec'}},
}

class Season(RichEnum):
    """
    Seasons of the year (Northern Hemisphere)
    """
    # Enum members
    SPRING = "SPRING"
    SUMMER = "SUMMER"
    AUTUMN = "AUTUMN"
    WINTER = "WINTER"

# Set metadata after class creation
Season._metadata = {
    "SPRING": {'description': 'Spring season', 'meaning': 'NCIT:C94731', 'annotations': {'months': 'Mar-May', 'astronomical_start': '~Mar 20'}},
    "SUMMER": {'description': 'Summer season', 'meaning': 'NCIT:C94732', 'annotations': {'months': 'Jun-Aug', 'astronomical_start': '~Jun 21'}},
    "AUTUMN": {'description': 'Autumn/Fall season', 'meaning': 'NCIT:C94733', 'annotations': {'months': 'Sep-Nov', 'astronomical_start': '~Sep 22', 'aliases': 'Fall'}},
    "WINTER": {'description': 'Winter season', 'meaning': 'NCIT:C94730', 'annotations': {'months': 'Dec-Feb', 'astronomical_start': '~Dec 21'}},
}

class TimePeriod(RichEnum):
    """
    Common time periods and intervals
    """
    # Enum members
    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    BIWEEKLY = "BIWEEKLY"
    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    SEMIANNUALLY = "SEMIANNUALLY"
    ANNUALLY = "ANNUALLY"
    BIANNUALLY = "BIANNUALLY"

# Set metadata after class creation
TimePeriod._metadata = {
    "HOURLY": {'description': 'Every hour', 'annotations': {'ucum': 'h'}},
    "DAILY": {'description': 'Every day', 'annotations': {'ucum': 'd'}},
    "WEEKLY": {'description': 'Every week', 'annotations': {'ucum': 'wk'}},
    "BIWEEKLY": {'description': 'Every two weeks', 'annotations': {'ucum': '2.wk'}},
    "MONTHLY": {'description': 'Every month', 'annotations': {'ucum': 'mo'}},
    "QUARTERLY": {'description': 'Every quarter (3 months)', 'annotations': {'ucum': '3.mo'}},
    "SEMIANNUALLY": {'description': 'Every six months', 'annotations': {'ucum': '6.mo'}},
    "ANNUALLY": {'description': 'Every year', 'annotations': {'ucum': 'a'}},
    "BIANNUALLY": {'description': 'Every two years', 'annotations': {'ucum': '2.a'}},
}

class TimeOfDay(RichEnum):
    """
    Common times of day
    """
    # Enum members
    DAWN = "DAWN"
    MORNING = "MORNING"
    NOON = "NOON"
    AFTERNOON = "AFTERNOON"
    EVENING = "EVENING"
    NIGHT = "NIGHT"
    MIDNIGHT = "MIDNIGHT"

# Set metadata after class creation
TimeOfDay._metadata = {
    "DAWN": {'description': 'Dawn (first light)', 'annotations': {'typical_time': '05:00-06:00'}},
    "MORNING": {'description': 'Morning', 'annotations': {'typical_time': '06:00-12:00'}},
    "NOON": {'description': 'Noon/Midday', 'annotations': {'typical_time': 720}},
    "AFTERNOON": {'description': 'Afternoon', 'annotations': {'typical_time': '12:00-18:00'}},
    "EVENING": {'description': 'Evening', 'annotations': {'typical_time': '18:00-21:00'}},
    "NIGHT": {'description': 'Night', 'annotations': {'typical_time': '21:00-05:00'}},
    "MIDNIGHT": {'description': 'Midnight', 'annotations': {'typical_time': '00:00'}},
}

class BusinessTimeFrame(RichEnum):
    """
    Common business and financial time frames
    """
    # Enum members
    REAL_TIME = "REAL_TIME"
    INTRADAY = "INTRADAY"
    T_PLUS_1 = "T_PLUS_1"
    T_PLUS_2 = "T_PLUS_2"
    T_PLUS_3 = "T_PLUS_3"
    END_OF_DAY = "END_OF_DAY"
    END_OF_WEEK = "END_OF_WEEK"
    END_OF_MONTH = "END_OF_MONTH"
    END_OF_QUARTER = "END_OF_QUARTER"
    END_OF_YEAR = "END_OF_YEAR"
    YEAR_TO_DATE = "YEAR_TO_DATE"
    MONTH_TO_DATE = "MONTH_TO_DATE"
    QUARTER_TO_DATE = "QUARTER_TO_DATE"

# Set metadata after class creation
BusinessTimeFrame._metadata = {
    "REAL_TIME": {'description': 'Real-time/instantaneous'},
    "INTRADAY": {'description': 'Within the same day'},
    "T_PLUS_1": {'description': 'Trade date plus one business day', 'annotations': {'abbreviation': 'T+1'}},
    "T_PLUS_2": {'description': 'Trade date plus two business days', 'annotations': {'abbreviation': 'T+2'}},
    "T_PLUS_3": {'description': 'Trade date plus three business days', 'annotations': {'abbreviation': 'T+3'}},
    "END_OF_DAY": {'description': 'End of business day', 'annotations': {'abbreviation': 'EOD'}},
    "END_OF_WEEK": {'description': 'End of business week', 'annotations': {'abbreviation': 'EOW'}},
    "END_OF_MONTH": {'description': 'End of calendar month', 'annotations': {'abbreviation': 'EOM'}},
    "END_OF_QUARTER": {'description': 'End of calendar quarter', 'annotations': {'abbreviation': 'EOQ'}},
    "END_OF_YEAR": {'description': 'End of calendar year', 'annotations': {'abbreviation': 'EOY'}},
    "YEAR_TO_DATE": {'description': 'From beginning of year to current date', 'annotations': {'abbreviation': 'YTD'}},
    "MONTH_TO_DATE": {'description': 'From beginning of month to current date', 'annotations': {'abbreviation': 'MTD'}},
    "QUARTER_TO_DATE": {'description': 'From beginning of quarter to current date', 'annotations': {'abbreviation': 'QTD'}},
}

class GeologicalEra(RichEnum):
    """
    Major geological eras
    """
    # Enum members
    PRECAMBRIAN = "PRECAMBRIAN"
    PALEOZOIC = "PALEOZOIC"
    MESOZOIC = "MESOZOIC"
    CENOZOIC = "CENOZOIC"

# Set metadata after class creation
GeologicalEra._metadata = {
    "PRECAMBRIAN": {'description': 'Precambrian (4.6 billion - 541 million years ago)'},
    "PALEOZOIC": {'description': 'Paleozoic Era (541 - 252 million years ago)'},
    "MESOZOIC": {'description': 'Mesozoic Era (252 - 66 million years ago)'},
    "CENOZOIC": {'description': 'Cenozoic Era (66 million years ago - present)'},
}

class HistoricalPeriod(RichEnum):
    """
    Major historical periods
    """
    # Enum members
    PREHISTORIC = "PREHISTORIC"
    ANCIENT = "ANCIENT"
    CLASSICAL_ANTIQUITY = "CLASSICAL_ANTIQUITY"
    MIDDLE_AGES = "MIDDLE_AGES"
    RENAISSANCE = "RENAISSANCE"
    EARLY_MODERN = "EARLY_MODERN"
    INDUSTRIAL_AGE = "INDUSTRIAL_AGE"
    MODERN = "MODERN"
    CONTEMPORARY = "CONTEMPORARY"
    DIGITAL_AGE = "DIGITAL_AGE"

# Set metadata after class creation
HistoricalPeriod._metadata = {
    "PREHISTORIC": {'description': 'Before written records'},
    "ANCIENT": {'description': 'Ancient history (3000 BCE - 500 CE)'},
    "CLASSICAL_ANTIQUITY": {'description': 'Classical antiquity (8th century BCE - 6th century CE)'},
    "MIDDLE_AGES": {'description': 'Middle Ages (5th - 15th century)'},
    "RENAISSANCE": {'description': 'Renaissance (14th - 17th century)'},
    "EARLY_MODERN": {'description': 'Early modern period (15th - 18th century)'},
    "INDUSTRIAL_AGE": {'description': 'Industrial age (1760 - 1840)'},
    "MODERN": {'description': 'Modern era (19th century - mid 20th century)'},
    "CONTEMPORARY": {'description': 'Contemporary period (mid 20th century - present)'},
    "DIGITAL_AGE": {'description': 'Digital/Information age (1950s - present)'},
}

__all__ = [
    "DayOfWeek",
    "Month",
    "Quarter",
    "Season",
    "TimePeriod",
    "TimeOfDay",
    "BusinessTimeFrame",
    "GeologicalEra",
    "HistoricalPeriod",
]