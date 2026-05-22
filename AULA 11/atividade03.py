# pip install pandas sqlalchemy pymysql
# ou
# python -m pip install pandas sqlalchemy pymysql
# executa o pip diretamente pela versão do Python que está ativa naquele momento.

# Caso tenha problema com scripts no PowerShell:
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser


from sqlalchemy import create_engine
import pandas as pd


# CONFIGURAÇÕES DE EXIBIÇÃO DO PANDAS
# quantidade máxima de linhas exibidas
pd.set_option('display.max_rows', 100)

# quantidade máxima de colunas exibidas
pd.set_option('display.max_columns', 20)

# largura máxima de colunas exidbidas em caracteres
pd.set_option('display.width', None)


# VARIÁVEIS DE CONEXÃO
host = 'localhost'
user = 'root'
password = '123456'
database = 'bd_aula11'



# CRIANDO A CONEXÃO COM O MYSQL
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')



# RECEBENDO OS DADOS DO BANCO
# read_sql() lê os dados da tabela tb_musicas através da conexão criada anteriormente
df_musicas = pd.read_sql('tb_musicas', engine)


# ------------------------------------------------------------------------------------------------
# EXIBINDO OS DADOS
# mostra as 5 primeiras linhas
print(df_musicas.head())
print()


# mostra apenas as colunas faixa e popularidade
print(df_musicas[['faixa', 'popularidade']])


# ------------------------------------------------------------------------------------------------
# MEDIDAS ESTATÍSTICAS
# maior popularidade
print(df_musicas['popularidade'].max())

# menor popularidade
print(df_musicas['popularidade'].min())

# média das popularidades
print(df_musicas['popularidade'].mean())

# média arredondada
print(round(df_musicas['popularidade'].mean(), 2))