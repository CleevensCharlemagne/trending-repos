import argparse
from trending_repos.api import fetch_repos
from trending_repos.duration_handler import (
    get_yesterday,
    get_first_day_month,
    get_first_day_week,
    get_first_day_year,
)

# Map CLI duration choices to their corresponding date functions.
# Functions are stored as callables (not called here) so the date
# is always computed fresh at runtime, not at import time.
TIME_RANGES = {
    "day": get_yesterday,
    "week": get_first_day_week,
    "month": get_first_day_month,
    "year": get_first_day_year,
}

def parse_args() -> argparse.Namespace:
    """Parse and return CLI arguments."""
    parser = argparse.ArgumentParser(description="Trending Github Repos CLI")

    # --duration: how far back to look. Defaults to 'week' whether the flag
    # is omitted entirely or used without a value (e.g. just --duration)
    parser.add_argument(
        "--duration",
        nargs="?",
        const='week',
        default='week',
        choices=TIME_RANGES.keys(),
        help="Time range for the displayed repos (default: week)"
    )

    # --limit: how many repos to return. Same default logic as --duration
    parser.add_argument(
        "--limit",
        nargs="?",
        const=10,
        default=10,
        type=int,
        help="Number of repositories to show (default: 10)"
    )

    return parser.parse_args()