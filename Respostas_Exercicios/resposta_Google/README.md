
# Google Search and Image Downloader

Este script Python automatiza a pesquisa no Google para um conjunto de termos (chaves) e extrai informações relevantes dos resultados. Ele também baixa as cinco primeiras imagens de cada termo de pesquisa do Google Images.

## Funcionalidades

-   Pesquisa no Google para cada termo fornecido.
-   Extrai o título e URL do primeiro resultado de pesquisa.
-   Baixa as cinco primeiras imagens de cada pesquisa no Google Images.
-   Salva os títulos e URLs em um arquivo CSV (`output.csv`).
-   Organiza as imagens baixadas em diretórios nomeados conforme os termos de pesquisa.

## Como Usar
   
1.  Instale o WebDriver apropriado para o navegador que você está usando (neste caso, Firefox).
2.  Coloque um arquivo CSV `pesquisa.csv` no diretório `./input`, contendo uma coluna 'Chave' com os termos de pesquisa.
3.  Execute o script Python:
    
    `python main.py` 
    
4.  Verifique o arquivo `output.csv` e a pasta `./output` para acessar os resultados e as imagens baixadas.

## Estrutura do Código

O script é dividido em várias funções para facilitar a compreensão e manutenção:

-   `setup_driver()`: Configura e retorna o driver do Selenium.
-   `search_google(driver, query)`: Realiza uma pesquisa no Google.
-   `get_first_result_data(driver, chave)`: Obtém dados do primeiro resultado de pesquisa.
-   `download_images(driver, chave)`: Baixa as primeiras 5 imagens para uma chave de pesquisa.
-   `save_image(data, path)`: Salva uma imagem de uma URL ou dados em base64.

## Dependências

-   Python 3.x
-   Pandas
-   Selenium
-   Requests
-   Tqdm

## Autor

Gustavo Garcia Pereira