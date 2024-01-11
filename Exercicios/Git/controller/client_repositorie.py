import requests

class RepositoriesController:

    def __init__(self, client_repositorie):
        self.client_repositorie = client_repositorie

    def handle(self):
    
        try:
            repositories_data = self.client_repositorie.get_response()
            repositories = self.client_repositorie.get_repositories(repositories_data)
            return repositories
        
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")