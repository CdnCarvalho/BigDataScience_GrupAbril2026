# lista vazia para armazenar os valores das vendas
vendas = []

# loop para cadastrar 10 vendas
for i in range(10):
    # solicita ao usuário o valor da venda
    valor = float(input(f"Digite o valor da venda {i+1}: "))
    
    # adiciona o valor informado na lista
    vendas.append(valor)

# exibe todos os valores cadastrados
print("\nLista de vendas:", vendas)

# definição das metas de comparação
META = 1000          # valor considerado como meta atingida
META_MINIMA = 700    # valor considerado próximo da meta

# percorre cada venda da lista para análise
for venda in vendas:
    
    # verifica se a venda atingiu a meta
    if venda >= META:
        print(f"\nParabéns! Meta atingida! \nA meta era de R$ {META}. \nA sua venda foi de R$ {venda}.")
    
    # verifica se a venda está próxima da meta
    elif venda >= META_MINIMA and venda < META:
        print(f"\nPróximo da meta. \nVocê não atingiu a meta principal, que era de R$ {META}.\nPorém conseguiu a meta mínima de R$ {META_MINIMA} \nA sua venda foi de R$ {venda}.")
    
    # caso não atinja nenhum dos critérios acima
    else:
        print(f"\nAbaixo das metas. \nNão bateu a meta principal de R$ {META}.\nTampouco a meta mínima de R$ {META_MINIMA} \nA sua venda foi de R$ {venda}.")