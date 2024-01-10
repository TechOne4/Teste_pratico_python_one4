import sqlite3
import pandas as pd

# Função para realizar consultas SQL
def execute_query(connection, query):
    return pd.read_sql_query(query, connection)

try:
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('data.sqlite')

    # Consultas SQL
    query_uf_populacao = 'SELECT uf, SUM(populacao) AS Populacao FROM data1 GROUP BY uf'
    query_capital_populacao = 'SELECT capital, populacao FROM data1 WHERE capital = municipio'
    query_regiao_populacao = 'SELECT d2.regiao, SUM(d1.populacao) AS Populacao FROM data1 d1 JOIN data2 d2 ON d1.uf = d2.uf GROUP BY d2.regiao'
    query_top_5_cidades = 'SELECT municipio, populacao FROM data1 ORDER BY populacao DESC LIMIT 5'
    query_estado_mais_municipios = '''
    SELECT d2.estado, SUM(d1.populacao) AS Populacao 
    FROM data1 d1 
    JOIN data2 d2 ON d1.uf = d2.uf 
    WHERE d2.uf = (SELECT uf FROM data2 ORDER BY qtd_mun DESC LIMIT 1) 
    GROUP BY d2.estado
    '''
    query_cidade_mais_populosa_por_estado = 'SELECT d2.estado, d1.municipio, MAX(d1.populacao) AS Populacao FROM data1 d1 JOIN data2 d2 ON d1.uf = d2.uf GROUP BY d2.estado'
    query_top_5_estados_municipios = 'SELECT estado, qtd_mun FROM data2 ORDER BY qtd_mun DESC LIMIT 5'

    # Executar as consultas
    uf_populacao = execute_query(conn, query_uf_populacao)
    capital_populacao = execute_query(conn, query_capital_populacao)
    regiao_populacao = execute_query(conn, query_regiao_populacao)
    top_5_cidades = execute_query(conn, query_top_5_cidades)
    estado_mais_municipios = execute_query(conn, query_estado_mais_municipios)
    cidade_mais_populosa_por_estado = execute_query(conn, query_cidade_mais_populosa_por_estado)
    top_5_estados_municipios = execute_query(conn, query_top_5_estados_municipios)

    # Criar um escritor do Pandas Excel
    with pd.ExcelWriter('output.xlsx') as writer:
        uf_populacao.to_excel(writer, sheet_name='UF x População', index=False)
        capital_populacao.to_excel(writer, sheet_name='Capital x População', index=False)
        regiao_populacao.to_excel(writer, sheet_name='Região x População', index=False)
        top_5_cidades.to_excel(writer, sheet_name='Top 5 Cidades', index=False)
        estado_mais_municipios.to_excel(writer, sheet_name='Estado com Mais Municípios', index=False)
        cidade_mais_populosa_por_estado.to_excel(writer, sheet_name='Cidade Mais Populosa por Estado', index=False)
        top_5_estados_municipios.to_excel(writer, sheet_name='Top 5 Estados com Mais Municípios', index=False)

finally:
    # Fechar a conexão com o banco de dados
    conn.close()
