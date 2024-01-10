
# Análise de Dados de População

Este script Python realiza a análise de dados populacionais de municípios e estados a partir de um banco de dados SQLite. Os resultados são exportados para um arquivo Excel com várias abas, cada uma contendo informações específicas relacionadas à população, como a população por UF, capital, região, entre outros.

## Funcionalidades

O script executa as seguintes análises e exporta os resultados para um arquivo Excel (`output.xlsx`):

1.  **UF x População**: População total por Unidade Federativa (UF).
2.  **Capital x População**: População das capitais.
3.  **Região x População**: População total por região.
4.  **Top 5 Cidades Mais Populosas**: Lista das 5 cidades com maior população.
5.  **Estado com Mais Municípios**: Estado com maior número de municípios e a sua população total.
6.  **Cidade Mais Populosa de Cada Estado**: Cidade mais populosa de cada estado.
7.  **Top 5 Estados com Mais Municípios**: Lista dos 5 estados com maior número de municípios.

## Como Usar

1.  Certifique-se de ter Python instalado em seu sistema.
    
2.  Coloque o banco de dados SQLite (nomeado `data.sqlite`) no mesmo diretório do script.
3.  Execute o script Python:
    
    `python main.py` 
    
4.  Após a execução, verifique o arquivo `output.xlsx` gerado no mesmo diretório para ver os resultados.

## Estrutura do Banco de Dados

O script espera duas tabelas principais no banco de dados `data.sqlite`:

-   `data1`: Contém informações de municípios, população e capitais.
-   `data2`: Contém informações de estados, UF, região e quantidade de municípios.

## Dependências

-   Python 3.x
-   Pandas
-   SQLite3

## Autor

Gustavo Garcia Pereira