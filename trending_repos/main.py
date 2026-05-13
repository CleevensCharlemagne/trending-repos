from trending_repos.cli import parse_args, TIME_RANGES
from trending_repos.api import fetch_repos

SEPARATOR = "-" * 40  # Visual divider printed between each repo

def main() -> None:
    """Entry point: parse arguments, fetch repos, and display results."""
    args = parse_args()

    # Call the date function mapped to the chosen duration to get the start date,
    # then pass it along with the limit to the API
    data = fetch_repos(TIME_RANGES[args.duration](), args.limit)

    # GitHub returns results under the "items" key
    for repo in data["items"]:
        print(f'Repo name: {repo["full_name"]}')
        print(f'Stars: {repo["stargazers_count"]}')
        print(f'Language: {repo["language"] or "N/A"}')  # language can be null on GitHub
        print(f'URL: {repo["html_url"]}')
        print(SEPARATOR)

if __name__ == '__main__':
    main()