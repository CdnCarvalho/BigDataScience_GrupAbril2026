# Função para calcular o desconto
def calcular_desconto(valor):
    desconto = valor * 0.16
    total = valor - desconto
    
    return total


# Entrada de dados
valor = float(input('Informe o valor da compra: R$ '))

# Verificando se possui desconto
if valor > 250:
    
    # Chamando a função para realizar o cálculo
    total_desconto = calcular_desconto(valor)
    
    print(f'Você ganhou 16% de DESCONTO.')
    print(f'Valor total com desconto: R$ {total_desconto:.2f}')

else:
    print(f'O valor total da compra é de: R$ {valor:.2f}')


print('Obrigado por comprar conosco. Volte sempre!')