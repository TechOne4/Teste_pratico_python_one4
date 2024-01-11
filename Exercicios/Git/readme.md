# Relatório de Repositórios Públicos no GitHub 

Este script Python solicita o nome de usuário do GitHub, lista todos os repositórios públicos desse usuário e exporta os dados para um arquivo Excel chamado output.xls. Os campos incluídos no arquivo são: `name_repo`, `url_repo`, `is_fork`, `size(Mb)`, `created_t`, `language`.


## Execução do Script

1. **Execute o script Python**
- Será solicitado que você insira o nome de usuário do GitHub.
- O script acessará a API do GitHub para obter informações sobre os repositórios públicos do usuário.
- Os dados serão processados e exportados para o arquivo output.xls.
- A data/nome do último repositório alterado será exibida no console.

## Pré-requisitos

- Python 3.x
- Virtualenv (opcional, mas recomendado)

## Instalação

1. **Clone o repositório:**

```bash```
- git clone https://github.com/seu-usuario/seu-projeto.git
- cd seu-projeto

2. **Crie e ative um ambiente virtual(opcional):**
- python -m venv venv
- source venv/bin/activate  # No Windows, use 'venv\Scripts\activate'

3. **Instale as dependências:**
```bash```
- pip install requirements.txt

4. **Utilização:**
- python main.py

# Logs 
Os logs de execução são armazenados no arquivo `./Logs/log.txt`.