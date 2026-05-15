# Função para calcular o bônus
def calcular_bonus(venda):
    
    bonus = venda * 0.10
    total = venda + bonus
    
    return bonus, total


# Entrada de dados
venda = float(input('Digite o valor da venda: R$ '))

# Verificando se ganhou bônus
if venda > 12000:
    
    # Chamando a função
    bonus, total_bonus = calcular_bonus(venda)
    
    print(f'\nValor da venda: R$ {venda:.2f}')
    print(f'Valor do bônus: R$ {bonus:.2f}')
    print(f'Valor total com bônus: R$ {total_bonus:.2f}')

else:
    print(f'\nValor da venda: R$ {venda:.2f}')
    print('Venda sem bônus.')