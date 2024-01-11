from typing import Dict, List
from requests import Request
import requests
from entities.repositorie import Repositories
from utils.log import LogWrapper


class ClientRepositorie:
    def __init__(self, username_github):
        self.host_repositorie = f"https://api.github.com/users/{username_github}/repos"
        self.logger = LogWrapper()

    def get_response(self) -> Request:
        response = requests.get(self.host_repositorie)
        self.logger.info(f"Status code: {response.status_code}")
        response.raise_for_status()  # Raise an exception if the request fails
        return response.json()

    def get_repositories(self, repositories_data: List[Dict[str, str]]) -> List[Dict[str, Repositories]]:
        
        repositories = []
        
        for repository in repositories_data:
            url_repo = repository['html_url']
            name_repo = repository['name']
            is_fork = repository['fork']
            size = repository['size']
            created_t = repository['created_at']
            language = repository['language']
            repositories.append({
                'url_repo': url_repo,
                'name_repo': name_repo,
                'is_fork': is_fork,
                'size': size,
                'created_t': created_t,
                'language': language
            })
            self.logger.info(f"Repositorie: {repositories[-1]}")
        return repositories