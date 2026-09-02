from __future__ import annotations
from datetime import datetime, timedelta, date
import random

def generate_dob(
    min_age: int = 1,
    max_age: int = 100,
    as_of: date | None = None,
    ) -> date:
    """
    :param min_age:
    :param max_age:
    :param as_of:
    :return:
    """
    if min_age < 0:
        raise ValueError('min_age must be >= 0')
    if max_age < min_age:
        raise ValueError('max_age cannot be less than min_age')
    as_of = as_of or date.now()

    latest_dob = _subtract_years(as_of, min_age)
    earliest_dob = _subtract_years(as_of, max_age)

    days = (latest_dob - earliest_dob).days

    return earliest_dob + timedelta(days=random.randint(0, days))

def _subtract_years(value: date, years: int) -> date:
    """Safely subtract years from a date"""
    try:
        return value.replace(year=value.year - years)
    except ValueError:
        return value.replace(year=value.year - years, day=28)