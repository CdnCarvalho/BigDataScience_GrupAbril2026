# ATIVIDADE 03 

# FUNÇÃO: calcula total e média
def calcular_vendas(lista_vendas):
    total = sum(lista_vendas)              # soma das vendas
    media = total / len(lista_vendas)      # calcula a média
    return total, media


# -----------------------------------
# PROGRAMA PRINCIPAL
contador = 1  # controle de vendedor

while True:
    print('\n' + 30 * '=')
    print(f'VENDEDOR {contador}')

    vendedor = input('Informe o nome do vendedor: ')
    vendas = []  # lista para armazenar as 4 vendas

    # coleta das 4 vendas usando for
    for i in range(4):
        valor = float(input(f'Informe a venda {i+1}: '))
        vendas.append(valor)

    # cálculo com função
    total, media = calcular_vendas(vendas)

    # saída
    print('\nRESULTADO:')
    print(f'Vendedor(a): {vendedor}')
    # todas as vendas
    print(f'As vendas foram: R$ {vendas}')
    # maior e menor venda
    print(f'Maior venda: R$ {max(vendas):.2f}')
    print(f'Menor venda: R$ {min(vendas):.2f}')
    print(f'Total de vendas: R$ {total:.2f}')
    print(f'Média de vendas: R$ {media:.2f}')

    # pergunta se deseja continuar
    opcao = input('\nDeseja informar outro vendedor? (S/N): ').strip().upper()

    # Entra no if, para qualquer caracter diferente de 'S'.
    # Só não entra, se o usuário digitar 'S'.
    if opcao != 'S':
        break

    contador += 1

print('\nPrograma encerrado.')
#  ------------------------------------------------------------------------------



# VERSÃO MAIS SIMPLES (sem listas e for interno)
# FUNÇÃO → recebe as vendas e calcula total e média
def calcular_vendas():
    # entrada das 4 vendas dentro da função
    v1 = float(input('Informe a venda 1: '))
    v2 = float(input('Informe a venda 2: '))
    v3 = float(input('Informe a venda 3: '))
    v4 = float(input('Informe a venda 4: '))

    # cálculo
    total = v1 + v2 + v3 + v4
    media = total / 4

    return total, media


# PROGRAMA PRINCIPAL
contador = 1

while True:
    print('\n' + 30 * '=')
    print(f'VENDEDOR {contador}')

    # chama a função (ela já faz entrada + cálculo)
    total, media = calcular_vendas()

    # saída
    print('\nRESULTADO:')
    print(f'Total de vendas: R$ {total:.2f}')
    print(f'Média de vendas: R$ {media:.2f}')

    # controle do loop
    opcao = input('\nDeseja cadastrar outro vendedor? (S/N): ').strip().upper()

    # Entra no if, para qualquer caracter diferente de 'S'.
    # Só não entra, se o usuário digitar 'S'.
    if opcao != 'S':
        break

    contador += 1

print('\nPrograma encerrado.')
# --------------------------------------------------------



# VERSÃO MAIS COMPLEXA (com listas e for interno)
# Não sabemos quantos vendedores e nem quantas vendas serão cadastradas
# -----------------------------------
# FUNÇÃO → calcula total e média
def calcular_vendas(lista_vendas):
    total = sum(lista_vendas)
    media = total / len(lista_vendas) if lista_vendas else 0
    return total, media



# -----------------------------------
# PROGRAMA PRINCIPAL

contador = 1  # controle de vendedores

while True:
    print('\n' + 30 * '=')
    print(f'VENDEDOR {contador}')
    
    vendedor = input('Informe o nome do vendedor: ')
    vendas = []  # lista para armazenar as vendas

    # ENTRADA DE VENDAS (quantidade desconhecida)
    while True:
        valor = float(input('Informe o valor da venda: '))
        vendas.append(valor)

        continuar_vendas = input('Deseja informar outra venda? (S/N): ').strip().upper()

        # Só NÃO entra no if, se o usuário digitar 'S'  
        if continuar_vendas != 'S':
            break


    # Chama a função para calcular total e média
    total, media = calcular_vendas(vendas)


    # SAÍDA
    print('\nRESULTADO:')
    print(f'Vendedor(a): {vendedor}')
    print(f'As vendas foram: R$ {vendas}')
    print(f'Quantidade de vendas: {len(vendas)}')
    print(f'Total de vendas: R$ {total:.2f}')
    print(f'Média de vendas: R$ {media:.2f}')


    # CONTROLE DE VENDEDORES
    continuar = input('\nDeseja cadastrar outro vendedor? (S/N): ').strip().upper()

    # Entra no if, para qualquer caracter diferente de 'S'.
    # Só não entra, se o usuário digitar 'S'.
    if continuar != 'S':
        break

    contador += 1

print('\nPrograma encerrado.')