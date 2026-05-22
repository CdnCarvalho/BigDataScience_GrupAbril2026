# pip install pandas sqlalchemy pymysql    ou   python -m pip install pandas sqlalchemy pymysql 
# # executa o pip diretamente pela versão do Python que está ativa naquele momento.

# Caso tenha Problema com scripts:
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
# ------------------------------------------------------------------------------------------------


from sqlalchemy import create_engine
import pandas as pd

# ------------------------------------------------------------------------------------------------
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 20)


# VARIÁVEIS DE CONEXÃO
host = 'localhost'
user = 'root'
password = '123456'
database = 'bd_aula11'



engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')


# RECEBENDO OS DADOS DO BANCO DE DADOS
df_roupas = pd.read_sql('tb_loja_roupas', engine)

print(df_roupas.head())
print(df_roupas[['descricao_produto', 'preco_venda']])


# # ------------------------------------------------------------------------------------------------
print(df_roupas['preco_venda'].max())  # maior valor
print(df_roupas['preco_venda'].min())  # menor valor
print(df_roupas['preco_venda'].mean())  # média
print(round(df_roupas['preco_venda'].mean(), 2))   # média arredondada


# # ------------------------------------------------------------------------------------------------
# df['total'] = df['preco'] * df['vendidos']  # Coluna do total arrecadado
# print(df[['produto', 'total']])  # mostra as colunas produto e total

# print(f'Arrecadação total: {df["total"].sum()}')  # Total geral