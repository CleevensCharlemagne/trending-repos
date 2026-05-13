from datetime import date, timedelta

# Each function calls date.today() internally so the date is always
# computed at call time, never cached at import time.

def get_first_day_month() -> str:
    """Return the first day of the current month as an ISO string."""
    today = date.today()
    return str(date(today.year, today.month, 1))

def get_first_day_week() -> str:
    """Return the date of the most recent Sunday as an ISO string."""
    today = date.today()
    # weekday() returns 0=Monday ... 6=Sunday.
    # This formula shifts to a Sunday-based week start.
    return str(today - timedelta(days=(today.weekday() + 1) % 7))

def get_first_day_year() -> str:
    """Return the first day of the current year as an ISO string."""
    return str(date(date.today().year, 1, 1))

def get_yesterday() -> str:
    """Return yesterday's date as an ISO string."""
    return str(date.today() - timedelta(days=1))