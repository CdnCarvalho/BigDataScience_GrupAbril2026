import pandas as pd

# Imprime linhas decorativas
def print_linhas():
    print(40*'---')


# Lendo um arquivo Excel com o método read_excel (deve apontar para o arquivo real)
df_vendas = pd.read_excel('vendas_eletronicos.xlsx')

# Exibindo as primeiras linhas do DataFrame
print("Primeiras linhas da planilha Excel:")
print(df_vendas.head())



# Valor máximo de faturamento total
print("\nMaior valor de faturamento total:")
print_linhas()
print(f'Maior: R$ {df_vendas['Faturamento Total (R$)'].max()}')

maior_faturamento = df_vendas['Faturamento Total (R$)'].max()
print(df_vendas[df_vendas['Faturamento Total (R$)'] == maior_faturamento][['Produto', 'Faturamento Total (R$)']])



# Valor menor de faturamento
print("\nMenor valor de faturamento:")
print_linhas()
print(f'Menor: R$ {df_vendas['Faturamento Total (R$)'].min()}')

menor_faturamento = df_vendas['Faturamento Total (R$)'].min()
print(df_vendas[df_vendas['Faturamento Total (R$)'] == menor_faturamento][['Produto', 'Faturamento Total (R$)']])


# Somatório das unidades vendidas
print("\nQuantidade de unidades vendidas:")
print_linhas()
print(f'Quantidade Total Vendida: {df_vendas['Unidades Vendidas'].sum()}')

# Média dos preços por unidade
print("\nMédia dos preços dos produtos:")
print_linhas()
print(f'Média entre os Preços: R$ {df_vendas['Preço por Unidade (R$)'].mean()}')

print('\nProdutos c/ unidades vendidas abaixo da média ')
print_linhas()
media = df_vendas['Unidades Vendidas'].mean()
print(df_vendas[df_vendas['Unidades Vendidas'] < media])