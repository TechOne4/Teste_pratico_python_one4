# Projeto de Captura de Dados do Google com Selenium

Este projeto utiliza Selenium para pesquisar no Google a partir de uma lista de chaves fornecidas em um arquivo CSV, capturar títulos e URLs, e salvar as 5 primeiras imagens de cada item em uma pasta específica.

## Pré-requisitos

- Python 3.x
- Virtualenv (opcional, mas recomendado)

## Instalação

1. **Clone o repositório:**

```bash```
- git clone https://github.com/leonardotideveloper/Teste_pratico_python_one4.git
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
Os logs de execução são armazenados no arquivo `log.txt` na raiz do projeto.

# Estrutura de arquivos
- `input/` contém o arquivo CSV de pesquisa.
- `output/` Local onde os resultados são salvos, incluindo subpastas para cada chave e imagens numeradas.
