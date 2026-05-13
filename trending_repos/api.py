import requests

def fetch_repos(time_range: str, limit: int) -> dict:
    """Fetch trending GitHub repositories created after the given date."""

    # Build the GitHub search query: filter by creation date, sort by stars
    url = f'https://api.github.com/search/repositories?q=created:>{time_range}&sort=stars&order=desc&per_page={limit}'

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an error for 4xx/5xx responses
        return response.json()
    except requests.exceptions.Timeout:
        raise SystemExit("Error: Request timed out.")
    except requests.exceptions.RequestException as e:
        raise SystemExit(f"Network error: {e}")