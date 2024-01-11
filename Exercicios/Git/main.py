
from controller.client_repositorie import RepositoriesController
from services.client_repositorie import ClientRepositorie
from utils.excel_generator import generate_excel_file


if __name__ == '__main__':
        
        try:
            username_github = input('Nome de Usuário: ')
        except KeyError as error:
              raise error
        
        github_repo = f"https://api.github.com/users/{username_github}/repos"
        cliente_repositorie = ClientRepositorie(username_github)
        repositorie_controller = RepositoriesController(cliente_repositorie)
        repositorie = repositorie_controller.handle()
        generate_excel_file(repositorie)

