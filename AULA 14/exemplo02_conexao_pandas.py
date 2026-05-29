# EXEMPLO 2 - Utilizando Pandas com SQLAlchemy
import pandas as pd
from sqlalchemy import create_engine

# pip install python-dotenv
from dotenv import load_dotenv
import os


load_dotenv() # Carrega as variáveis do arquivo dot.env

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_DATABASE')
# -------------------------------------------------------------



# Query SQL
query = "SELECT * FROM cadastro_produtos"


# URL de conexão com o banco
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')


# Lê os dados do banco e transforma em DataFrame
df_produtos = pd.read_sql(query, engine)
print(df_produtos)
