# pip install pandas sqlalchemy pymysql
from sqlalchemy import create_engine
import pandas as pd


# pip install python-dotenv
from dotenv import load_dotenv
import os



def conecta_banco():
    # Variáveis de conexão com o banco
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_DATABASE')

    # URL de conexão com o banco
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
    return engine



load_dotenv() # Carrega as variáveis do arquivo dot.env

engine = conecta_banco()


# Leitura das tabelas do MySQL
try:

    # Leitura das tabelas diretamente do banco
    df_usuarios = pd.read_sql('tb_usuarios', engine)
    df_livros = pd.read_sql('tb_livros', engine)
    df_itens_alugados = pd.read_sql('tb_itens_alugados', engine)
    df_alugados = pd.read_sql('tb_alugados', engine)

except Exception as e:
    print(f'Erro ao acessar o banco de dados: {e}')


# Relacionando as tabelas com merge
try:

    # =========================================================
    # MERGE 1
    # Junta os livros com os itens alugados usando a coluna id_livro
    df_merge1 = pd.merge(
        df_livros, df_itens_alugados, on='id_livro'
    )


    # =========================================================
    # MERGE 2
    # Junta o resultado anterior com a tabela de alugados usando a coluna id_aluguel
    df_merge2 = pd.merge(
        df_merge1, df_alugados, on='id_aluguel'
    )


    # =========================================================
    # MERGE FINAL
    # Junta o resultado anterior com os usuários usando a coluna id_usuario
    df_dados = pd.merge(
        df_merge2, df_usuarios, on='id_usuario'
    )


    # =========================================================
    # FILTRO
    # Mostra apenas devoluções realizadas em novembro
    filtro = (
        (df_dados['data_devolucao'] >= '2024-11-01') &
        (df_dados['data_devolucao'] <= '2024-11-30')
    )

    df_novembro = df_dados[filtro]


    # =========================================================
    # RESULTADO FINAL
    # =========================================================
    print('\nRelatório de Livros Alugados em Novembro:\n')

    print(
        df_novembro[
            [
                'id_usuario',
                'nome',
                'data_aluguel',
                'data_devolucao',
                'valor',
                'id_livro',
                'titulo',
                'id_aluguel'
            ]
        ]
    )

    print()
    print(df_final[
            [
                'id_usuario',
                'nome',
                'data_aluguel',
                'data_devolucao',
                'valor',
                'id_livro',
                'titulo',
                'id_aluguel'
            ]
        ])
except Exception as e:
    print(f'Erro ao processar as informações: {e}')