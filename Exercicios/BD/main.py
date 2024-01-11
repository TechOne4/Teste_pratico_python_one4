import sqlite3
import pandas as pd
from log import log_wrapper

# Interface para a estratégia de geração de relatórios
class ReportStrategy:
    def generate_report(self, df, writer):
        pass

# Estratégia para o relatório UF x Populacao
class UFPopulationReport(ReportStrategy):
    @log_wrapper
    def generate_report(self, df, writer, df_data2=None):
        df_uf_populacao = df.groupby('uf')['populacao'].sum().reset_index()
        df_uf_populacao.to_excel(writer, sheet_name='UF x Populacao', index=False)

# Estratégia para o relatório Capital x Populacao
class CapitalPopulationReport(ReportStrategy):
    @log_wrapper
    def generate_report(self, df, writer, df_data2=None):
        df_capital_populacao = df[df['capital'] == 'Capital'][['municipio', 'populacao']]
        df_capital_populacao.to_excel(writer, sheet_name='Capital x Populacao', index=False)

# Estratégia para o relatório Regiao x Populacao
class RegionPopulationReport(ReportStrategy):
    @log_wrapper
    def generate_report(self, df, writer, df_data2):
        df_regiao_populacao = pd.merge(df, df_data2[['uf', 'regiao']], on='uf')
        df_regiao_populacao = df_regiao_populacao.groupby('regiao')['populacao'].sum().reset_index()
        df_regiao_populacao.to_excel(writer, sheet_name='Regiao x Populacao', index=False)

# Estratégia para o relatório Top 5 Cidades Populosas
class Top5CitiesReport(ReportStrategy):
    @log_wrapper
    def generate_report(self, df, writer, df_data2=None):
        df_top5_cidades = df.nlargest(5, 'populacao')[['municipio', 'populacao']]
        df_top5_cidades.to_excel(writer, sheet_name='Top 5 Cidades Populosas', index=False)

# Estratégia para o relatório Estado com mais Municipios
class StateWithMostMunicipalitiesReport(ReportStrategy):
    @log_wrapper
    def generate_report(self, df, writer, df_data2):
        estado_mais_municipios = df_data2.loc[df_data2['qtd_mun'].idxmax(), 'estado']
        uf = df_data2[df_data2['estado'] == estado_mais_municipios]['uf'].unique()[0]
        populacao_estado_mais_municipios = df[df['uf'] == uf]['populacao'].sum()
        df_estado_mais_municipios = pd.DataFrame({'Estado': [estado_mais_municipios], 'Populacao': [populacao_estado_mais_municipios]})
        df_estado_mais_municipios.to_excel(writer, sheet_name='Estado com mais Municipios', index=False)
        return True

# Estratégia para o relatório Cidade mais Populosa por Estado
class MostPopulousCityByStateReport(ReportStrategy):
    @log_wrapper
    def generate_report(self, df, writer, df_data2=None):
        df_cidade_mais_populosa_por_estado = df.loc[df.groupby('uf')['populacao'].idxmax(), ['uf', 'municipio', 'populacao']]
        df_cidade_mais_populosa_por_estado.to_excel(writer, sheet_name='Cidade mais Populosa por Estado', index=False)

# Estratégia para o relatório Top estados com mais Municipios
class Top5StatesWithMostMunicipalitiesReport(ReportStrategy):
    @log_wrapper
    def generate_report(self, df, writer, df_data2=None):
        df_top5_estados_municipios = df.nlargest(5, 'qtd_mun')[['estado', 'qtd_mun']]
        df_top5_estados_municipios.to_excel(writer, sheet_name='Top estados com mais Municipios', index=False)

# Classe Context para gerar relatórios
class ReportGenerator:
    def __init__(self, strategy):
        self.strategy = strategy

    def generate_report(self, df, writer, df_data2=None):
        self.strategy.generate_report(df, writer, df_data2)

if __name__ == "__main__":
    connection = sqlite3.connect('data.sqlite')

    query_data1 = "SELECT * FROM data1"
    query_data2 = "SELECT * FROM data2"

    df_data1 = pd.read_sql_query(query_data1, connection)
    df_data2 = pd.read_sql_query(query_data2, connection)

    df_data1['populacao'] = pd.to_numeric(df_data1['populacao'], errors='coerce')

    # Criar instâncias das estratégias
    uf_population_strategy = UFPopulationReport()
    capital_population_strategy = CapitalPopulationReport()
    region_population_strategy = RegionPopulationReport()
    top5_cities_strategy = Top5CitiesReport()
    state_with_most_municipalities_strategy = StateWithMostMunicipalitiesReport()
    most_populous_city_by_state_strategy = MostPopulousCityByStateReport()
    top5_states_with_most_municipalities_strategy = Top5StatesWithMostMunicipalitiesReport()

    # Criar instâncias do ReportGenerator com as estratégias desejadas
    uf_population_reporter = ReportGenerator(uf_population_strategy)
    capital_population_reporter = ReportGenerator(capital_population_strategy)
    region_population_reporter = ReportGenerator(region_population_strategy)
    top5_cities_reporter = ReportGenerator(top5_cities_strategy)
    state_with_most_municipalities_reporter = ReportGenerator(state_with_most_municipalities_strategy)
    most_populous_city_by_state_reporter = ReportGenerator(most_populous_city_by_state_strategy)
    top5_states_with_most_municipalities_reporter = ReportGenerator(top5_states_with_most_municipalities_strategy)


    with pd.ExcelWriter('output.xls', engine='xlsxwriter') as writer:

        # Aplicar as estratégias para gerar os relatórios
        uf_population_reporter.generate_report(df_data1, writer)
        capital_population_reporter.generate_report(df_data1, writer)
        region_population_reporter.generate_report(df_data1, writer, df_data2)
        top5_cities_reporter.generate_report(df_data1, writer)
        state_with_most_municipalities_reporter.generate_report(df_data1, writer, df_data2)
        most_populous_city_by_state_reporter.generate_report(df_data1, writer)
        top5_states_with_most_municipalities_reporter.generate_report(df_data2, writer)
