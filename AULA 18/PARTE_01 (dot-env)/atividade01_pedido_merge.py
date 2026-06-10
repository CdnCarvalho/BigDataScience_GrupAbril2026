# Liste os pedidos feitos por clientes que moram em São Paulo.
# pip install sqlalchemy pymysql pandas
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

# LEITURA DAS TABELAS
try:

    # Tabela de clientes
    df_clientes = pd.read_sql('tb_clientes', engine)

    # Tabela de pedidos
    df_pedidos = pd.read_sql('tb_pedidos', engine)

    # Tabela de itens do pedido
    df_itens = pd.read_sql('tb_itens', engine)

    # Tabela de produtos
    df_produtos = pd.read_sql('tb_produtos', engine)


    # # =========================================================================
    # # RENOMEANDO COLUNAS
    # # Para que os merges possam usar apenas ON
    # # =========================================================================

    # # cliente_codigo => codigo_cliente
    # df_pedidos = df_pedidos.rename(
    #     columns={'cliente_codigo': 'codigo_cliente'}
    # )

    # # pedido_codigo => codigo_pedido
    # df_itens = df_itens.rename(
    #     columns={'pedido_codigo': 'codigo_pedido'}
    # )


except Exception as e:
    print(f'Erro ao conectar ou consultar o banco: {e}')



# RELACIONAMENTOS COM MERGE
try:
    # MERGE 1: Junta clientes com pedidos usando a coluna codigo_cliente
    df_merge1 = pd.merge(df_clientes, df_pedidos, on='codigo_cliente')


    # MERGE 2: Junta pedidos com itens do pedido usando a coluna codigo_pedido
    df_merge2 = pd.merge(df_merge1,df_itens, on='codigo_pedido')


    # MERGE FINAL: Junta com a tabela de produtos usando a coluna codigo_produto
    df_final = pd.merge(df_merge2, df_produtos, on='codigo_produto')


    # FILTRO: Mostrar apenas clientes da cidade de São Paulo
    df_sao_paulo_curitiba = df_final[
       ( 
           (df_final['cidade'] == 'Sao Paulo') |
           (df_final['cidade'] == 'Curitiba')
        
        )
    ]




    # RESULTADO FINAL
    print('\nPedidos de Clientes de São Paulo:\n')

    print(
        df_sao_paulo_curitiba[
            [
                'codigo_cliente', 'nome', 'sobrenome', 'cidade',
                'codigo_pedido', 'data_pedido', 'valor',
                'produto'                
            ]
        ]
    )



    # #### DESAFIO ################################################################
    df_sp_curitiba_eletronicos = df_final.query(
        '(cidade == "Sao Paulo" | cidade == "Curitiba") & categoria == "Eletronicos"'
    )


    # ##### IMPRESSÃO DO DESAFIO #####################################################
    print('\nPedidos da Categoria Eletrônicos a partir das cidade de São Paulo e Couritiba:\n')

    print(
        df_sp_curitiba_eletronicos[
            [
                'codigo_cliente', 'nome', 'sobrenome', 'cidade',
                'codigo_pedido', 'data_pedido', 'valor',
                'produto', 'categoria'                
            ]
        ]
    )

except Exception as e:
    print(f'Erro ao processar as informações: {e}')




    # # =========================================================================
    # Quando os nomes das colunas são diferentes é necessário informar o parâmetro left on e right_on
    # df_merge1 = pd.merge(
    #     df_clientes,
    #     df_pedidos,
    #     left_on='codigo_cliente',
    #     right_on='cliente_codigo'
    # )


    # # =========================================================================
    # # MERGE 2
    # # Junta pedidos com itens do pedido
    # # usando:
    # # tb_pedidos.codigo_pedido = tb_itens.pedido_codigo
    # # =========================================================================
    # df_merge2 = pd.merge(
    #     df_merge1,
    #     df_itens,
    #     left_on='codigo_pedido',
    #     right_on='pedido_codigo'
    # )


    # # =========================================================================
    # # MERGE FINAL
    # # Junta com a tabela de produtos
    # # usando:
    # # produtos.codigo_produto = tb_itens.codigo_produto
    # # =========================================================================
    # df_final = pd.merge(
    #     df_merge2,
    #     df_produtos,
    #     on='codigo_produto'
    # )