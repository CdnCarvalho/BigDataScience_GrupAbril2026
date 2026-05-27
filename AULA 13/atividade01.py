import pandas as pd

# Passo 1: Carregando a planilha de vendas de uma loja de roupas
df_roupas = pd.read_excel('vendas_roupas.xlsx')

# Passo 2: Exibindo as 10 primeiras linhas da planilha
print("\nAs primeiras 10 linhas da planilha:")
print(10 * '=')
print(df_roupas.head(10))


# Somatório das unidades vendidas
print("\nSomatório das unidades vendidas:")
print(45 * '=')
print(df_roupas['Unidades Vendidas'].sum())


# Média dos preços por unidade
print("\nMédia dos preços dos produtos:")
print(45 * '=')
print(df_roupas['Preco por Unidade (R$)'].mean())


# Maior valor de faturamento total
print("\nMaior valor de faturamento total:")
print(45 * '=')
print(df_roupas['Faturamento Total (R$)'].max())
print(df_roupas.loc[df_roupas['Faturamento Total (R$)'].idxmax(), 'Produto'])  # Mostra apenas o nome do produto de menor valor
print(df_roupas.loc[df_roupas['Faturamento Total (R$)'].idxmax()])  # Mostra todas as informações da linha do menor valor


# Menor faturamento total
print("\nMenor valor de Faturamento total:")
print(45 * '=')
print(df_roupas['Faturamento Total (R$)'].min())
print(df_roupas.loc[df_roupas['Faturamento Total (R$)'].idxmin(), 'Produto'])  # Mostra apenas o nome do produto de menor valor
print(df_roupas.loc[df_roupas['Faturamento Total (R$)'].idxmin()])  # Mostra todas as informações da linha do menor valor


# Menor nível de satisfação (BAIXO)
print("\nProdutos com menores níveis de satisfação:")
print(120 * '=')
print(df_roupas[df_roupas['Satisfacao'] == 'BAIXO'])



# Menor nível de satisfação (MUITO ALTO)
print("\nProdutos com menores níveis de satisfação:")
print(120 * '=')
print(df_roupas[df_roupas['Satisfacao'] == 'MUITO ALTO'])


# Produtos com faturamento acima da média
print("\nProdutos acima da média de faturamento:")
print(120 * '=')
media = df_roupas['Faturamento Total (R$)'].mean()
print(df_roupas.loc[df_roupas['Faturamento Total (R$)'] >= media])

# ------------------------------------ Somente até aqui -----------------------------------------------------------

# salvar em um arquivo csv
df_roupas_baixo = df_roupas[df_roupas['Satisfacao'] == 'BAIXO']
df_roupas_baixo.to_csv('roupas_baixo.csv', index=False)