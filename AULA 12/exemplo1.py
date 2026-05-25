import pandas as pd

# Criando uma lista de quantidades em estoque para diferentes produtos
produtos = ['Notebook', 'Smartphone', 'Tablet', 'Smartwatch', 'Câmera', 'Notebook']
lista_estoque = [16, 28, 19, 13, 26, 9]


# ----------------------------------------------- Série de dados - Padrão x Listas
serie_padrao = pd.Series(lista_estoque)
print('\nSéries do Pandas - Modo Padrão')
print(30*'-')
print(serie_padrao)
print(serie_padrao[0])
print(serie_padrao[[1, 3]])
print(serie_padrao + 100)
print(serie_padrao[serie_padrao >= 18])



# ----------------------------------------------- Série de dados - Personalizada
print('\nSéries c/ índices Personalizados')
print(30*'-')
estoque = pd.Series(lista_estoque, index=produtos)

# Exibindo a série
print("\nSérie Estoque de Produtos:")
print(estoque)

# Selecionando um valor específico pelo índice
print("\nQuantidade de notebooks em estoque:")
print(estoque['Notebook'])

# # Selecionando múltiplos valores
print("\nEstoque de Notebook e Câmera:")
print(estoque[['Notebook', 'Câmera']].values)  # Mostra apenas os valores
print(estoque[['Notebook', 'Câmera']])  # Mostra com os índices


# --------------------------------------------- Operação aritmética: 
# Incluindo um valor nulo para simular a falta de dados
estoque['Headphone'] = None  # Em casos reais, é melhor prática é usar da seguinte maneira estoque.loc['Headphone'] = None
print("\nEstoque com um valor nulo (Headphone):")
print(estoque)

# Aumentar estoque em 5 unidades
print('\nSuporte a Operações com NaN')
print("\nAumentando o estoque em 5 unidades para todos os produtos:")
print(estoque + 5)


# -------------------------------------------- Operações Aritméticas entre Séries 
lista_precos = [3500, 2500, 1200, 900, 1500, 2600]
precos = pd.Series(lista_precos, index=produtos)

# # Calculando o valor total do estoque (preço * quantidade)
print("\nValor total do estoque por produto (preço * quantidade):")
print(precos * estoque)


# ---------------------------------------------- Outros Métodos de Filtro
# Filtrando por índices "que são textos"
# print('\nProdutos no estoque, que iniciam com Smart')
# print(estoque[estoque.index.str.startswith('Smart')])  # Inicia com Smart
# print(estoque[estoque.index.str.contains('Smart')])  # Contém Smart
# print(estoque[estoque.index.str.endswith('phone')])  # Finaliza dom phone