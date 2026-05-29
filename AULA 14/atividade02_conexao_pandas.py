# EXEMPLO 2
from sqlalchemy import create_engine, text
import pandas as pd

from dotenv import load_dotenv
import os

load_dotenv() # Carrega as variáveis do arquivo dot.env


def conecta_banco():
    # Variáveis de conexão com o banco
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_DATABASE')

    # URL de conexão com o banco, usando SQLAlchemy e PyMySQL
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
    return engine



engine = conecta_banco()
query = "SELECT * FROM materiais_construcao"

df_materiais = pd.read_sql(query, engine)  
print(df_materiais)

