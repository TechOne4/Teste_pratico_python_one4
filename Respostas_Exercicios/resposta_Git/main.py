import requests
import pandas as pd
from datetime import datetime


def get_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def extract_repo_data(repos):
    repo_data = []
    last_modified = datetime.min
    last_repo = ""

    for repo in repos:
        repo_info = {
            'name_repo': repo['name'],
            'url_repo': repo['html_url'],
            'is_fork': repo['fork'],
            'size(Mb)': repo['size'] / 1024,
            'created_t': repo['created_at'],
            'language': repo['language']
        }
        repo_data.append(repo_info)

        # Check for the last modified repository
        last_push = datetime.strptime(repo['pushed_at'], '%Y-%m-%dT%H:%M:%SZ')
        if last_push > last_modified:
            last_modified = last_push
            last_repo = repo['name']

    return repo_data, last_repo, last_modified


def save_to_excel(data, filename="output.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)


def main():
    username = input("Enter GitHub username: ")
    repos = get_github_repos(username)
    if repos:
        repo_data, last_repo, last_modified = extract_repo_data(repos)
        save_to_excel(repo_data)
        print(f"Last modified repository: {last_repo} on {last_modified}")
    else:
        print("Failed to fetch repositories. Please check the username.")


if __name__ == "__main__":
    main()
