
# GitHub Repositories Data Extractor

Este script Python permite extrair informações sobre os repositórios públicos de um usuário do GitHub e exportá-las para um arquivo Excel. Ele fornece detalhes como nome do repositório, URL, se é um fork, tamanho, data de criação, e linguagem de programação utilizada.

## Funcionalidades

-   Extrai informações de todos os repositórios públicos de um usuário específico do GitHub.
-   Calcula qual foi o último repositório modificado pelo usuário.
-   Exporta os dados coletados para um arquivo Excel (`output.xlsx`).

## Como Usar
    
1.  Execute o script e insira o nome de usuário do GitHub quando solicitado:
    
    `python main.py` 
    
2.  Verifique o arquivo `output.xlsx` gerado para acessar as informações extraídas.

## Estrutura do Código

O script é dividido em várias funções para facilitar a manutenção e a compreensão:

-   `get_github_repos(username)`: Faz uma chamada à API do GitHub para obter os repositórios do usuário.
-   `extract_repo_data(repos)`: Processa os dados JSON obtidos e extrai as informações relevantes.
-   `save_to_excel(data, filename)`: Salva os dados extraídos em um arquivo Excel.

## Dependências

-   Python 3.x
-   Pandas
-   Requests

## Autor

Gustavo Garcia Pereira