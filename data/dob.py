from __future__ import annotations

import random
from datetime import date, timedelta

# In-universe "today" — character creation always happens as of this date.
# Real Gregorian months/days are kept, just with the year set far into the
# future (7777) to reflect the setting's calendar.
CURRENT_DATE = date(7777, 1, 1)

MIN_AGE = 0
MAX_AGE = 80


def generate_dob(
        min_age: int = MIN_AGE,
        max_age: int = MAX_AGE,
        as_of: date | None = None,
) -> date:
    """
    Generate a date of birth using real-world month/day numbering, but
    anchored to the in-universe year 7777. Birth year will always fall
    within [as_of.year - max_age, as_of.year - min_age] — by default
    that's 7697-7777, per the setting's 80-year window.

    :param min_age: youngest allowed age (inclusive)
    :param max_age: oldest allowed age (inclusive) — defaults to 80,
        the setting's hard limit ("doesn't accept 80 years before and
        after 7777")
    :param as_of: reference date to calculate age from; defaults to
        CURRENT_DATE (Jan 1, 7777), not real-world today
    :return: a randomly generated date of birth within the given age range
    """
    if min_age < 0:
        raise ValueError('min_age must be >= 0')
    if max_age < min_age:
        raise ValueError('max_age cannot be less than min_age')
    as_of = as_of or CURRENT_DATE

    latest_dob = _subtract_years(as_of, min_age)
    earliest_dob = _subtract_years(as_of, max_age)

    days = (latest_dob - earliest_dob).days
    return earliest_dob + timedelta(days=random.randint(0, days))


def format_dob(dob: date) -> str:
    """Numeric display format, e.g. '03/17/7712'."""
    return dob.strftime("%m/%d/%Y")


def _subtract_years(value: date, years: int) -> date:
    """Safely subtract years from a date (handles Feb 29 by falling back to Feb 28)."""
    try:
        return value.replace(year=value.year - years)
    except ValueError:
        return value.replace(year=value.year - years, day=28)
