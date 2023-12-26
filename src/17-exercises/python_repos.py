import requests

def get_response():
    """Make an API call, and return the response."""
    url = 'https://api.github.com/search/repositories?q=language:python&sort='\
        'stars'
    headers = {'Accepts': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    return r

def get_repo_dicts(r):
    """Return a set of dicts representing the most populat repositories."""
    response_dict = r.json()
    repo_dicts = response_dict['items']
    return repo_dicts

def print_selected_info(repo_dicts):
    """Displays selected information about each repository."""
    print("\nSelected information about each repository:")
    for repo_dict in repo_dicts:
        print(f"\nName: {repo_dict['name']}")
        print(f"Owner: {repo_dict['owner']['login']}")
        print(f"Stars: {repo_dict['stargazers_count']}")
        print(f"Repository: {repo_dict['html_url']}")
        print(f"Description: {repo_dict['description']}")

if __name__ == "__main__":
    r = get_response()
    repo_dicts = get_repo_dicts(r)
    print_selected_info(repo_dicts)