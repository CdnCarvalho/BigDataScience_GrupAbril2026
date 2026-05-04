# ======================================
# ####### EXEMPLO - Maior e Menor valor


# ENTRADA DE DADOS
# O usuário informa dois números
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))



# -------------------------------------
# PROCESSAMENTO
# Verificamos qual número é maior e qual é menor
if n1 > n2:
    maior = n1
    menor = n2
    # print(f'O maior é {maior} e o menor é {menor}')

elif n2 > n1:
    maior = n2
    menor = n1
    # print(f'O maior é {maior} e o menor é {menor}')

else:
    # Caso os dois números sejam iguais
    igual = True
    # print(f'Os dois números são iguais.')



# -------------------------------------
# SAÍDA DE DADOS
print('\nRESULTADO:')

# Se os números forem iguais, informamos isso
if igual == True:
    print('Os dois números são iguais.')
else:
    print(f'Maior número: {maior}')
    print(f'Menor número: {menor}')