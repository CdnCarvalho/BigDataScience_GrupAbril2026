# ==============================================================================
# FUNÇÕES ESPECIALISTAS
# ==============================================================================

def calcular_vendas(lista_vendas):
    """Calcula estritamente o total acumulado e a média das vendas."""
    total = sum(lista_vendas)
    media = total / len(lista_vendas) if lista_vendas else 0
    return total, media


def mostrar_resultado(vendedor, lista_vendas, total, media):
    """Exibe o relatório formatado das vendas na tela."""
    print('\n' + 15 * '-')
    print('RELATÓRIO DE VENDAS:')
    print(f'Vendedor(a): {vendedor}')
    print(f'As vendas foram: R$ {lista_vendas}')
    print(f'Quantidade de vendas: {len(lista_vendas)}')
    print(f'Total de vendas: R$ {total:.2f}')
    print(f'Média de vendas: R$ {media:.2f}')


# ==============================================================================
# FUNÇÃO ORQUESTRADORA (Centraliza o fluxo do vendedor)
# ==============================================================================

def processar_vendas_vendedor(vendedor, lista_vendas):
    """Valida os dados, coordena os cálculos e aciona a exibição do resultado."""
    
    # 1. VALIDAÇÃO EXPLÍCITA (Sem embutir função no if)
    for valor in lista_vendas:
        if valor < 0:
            print(f'\n[ERRO] {vendedor} possui venda com valor inválido (R$ {valor}).')
            print('O relatório deste vendedor não pôde ser gerado.')
            return  # Encerra a funçãoe volta para o programa principal
            
    # CHAMADA DA FUNÇÃO (Cálculo)
    total_vendas, media_vendas = calcular_vendas(lista_vendas)
    
    # 3. CHAMADA DA FUNÇÃO (Exibição)
    mostrar_resultado(vendedor, lista_vendas, total_vendas, media_vendas)


# ==============================================================================
# PROGRAMA PRINCIPAL
# ==============================================================================
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
        if continuar_vendas != 'S':
            break

    # CHAMADA ÚNICA: Passamos a responsabilidade para a função orquestradora
    processar_vendas_vendedor(vendedor, vendas)

    # CONTROLE DE VENDEDORES
    continuar = input('\nDeseja cadastrar outro vendedor? (S/N): ').strip().upper()
    if continuar != 'S':
        break

    contador += 1

print('\nPrograma encerrado.')