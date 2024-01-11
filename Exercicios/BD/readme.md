# Projeto de Captura de Dados do Google com Selenium

Este script Python utiliza o banco de dados data.sqlite para gerar diversos relatórios e exportá-los para um arquivo Excel (output.xls). Cada relatório é gerado usando uma estratégia específica, implementada como uma classe derivada da classe abstrata ReportStrategy. A seguir, são apresentadas as estratégias e os relatórios gerados:

## Estratégias de Relatório

1. **UF x População**
- **Classe**: `UFPopulationReport`
- **Método**: `generate_report`
- **Descrição**: Agrupa o DataFrame pela unidade federativa (UF) e calcula a soma da população para cada UF. O resultado é  exportado para a aba 'UF x População' no arquivo Excel.

2. **Capital x População**
- **Classe**: `CapitalPopulationReport`
- **Método**: `generate_report`
- **Descrição**: Filtra o DataFrame para incluir apenas as linhas referentes às capitais e extrai as colunas 'municipio' e 'populacao'. O resultado é exportado para a aba 'Capital x População' no arquivo Excel.

3. **Região x População**
- **Classe**: `RegionPopulationReport`
- **Método**: `generate_report`
- **Descrição**: Realiza um merge entre o DataFrame principal (df) e um segundo DataFrame (df_data2) utilizando a coluna 'uf'. Em seguida, agrupa o DataFrame resultante pela coluna 'regiao' e calcula a soma da população para cada região. O resultado é exportado para a aba 'Região x População' no arquivo Excel.

4. **Top 5 Cidades Populosas**
- **Classe**: `Top5CitiesReport`
- **Método**: `generate_report`
- **Descrição**: Seleciona as cinco cidades com maior população e extrai as colunas 'municipio' e 'populacao'. O resultado é exportado para a aba 'Top 5 Cidades Populosas' no arquivo Excel.

5. **Estado com Mais Municípios**
- **Classe**: `StateWithMostMunicipalitiesReport`
- **Método**: `vgenerate_report`
- **Descrição**: Identifica o estado com o maior número de municípios, obtém a UF correspondente e calcula a população total desse estado. O resultado é exportado para a aba 'Estado com mais Municípios' no arquivo Excel.

6. **Cidade mais Populosa por Estado**
**Classe**: `MostPopulousCityByStateReport`
**Método**: `generate_report`
**Descrição**: Para cada estado, identifica a cidade mais populosa e extrai as colunas 'uf', 'municipio' e 'populacao'. O resultado é exportado para a aba 'Cidade mais Populosa por Estado' no arquivo Excel.

7. **Top 5 Estados com Mais Municípios**
**Classe**: `Top5StatesWithMostMunicipalitiesReport`
**Método**: `generate_report`
**Descrição**: Seleciona os cinco estados com o maior número de municípios e extrai as colunas 'estado' e 'qtd_mun'. O resultado é exportado para a aba 'Top estados com mais Municípios' no arquivo Excel.

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
