#  Desenvolver  um programa que peça  um número e calcule o dobro, triplo e o quadrado
#  do número informado pelo usuário.

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
quadrado = numero ** 2

print(f'O dobro de {numero} é {dobro}')
print(f'O triplo de {numero} é {triplo}')
print(f'O quadrado de {numero} é {quadrado}')
# ----------------------------------------------------------------------------------



# Se precisarmo de fazer isso dez vezes?
for i in range(10):
    numero = int(input('Digite um número: '))
    dobro = numero * 2
    triplo = numero * 3
    quadrado = numero ** 2

    print(f'O dobro de {numero} é {dobro}')
    print(f'O triplo de {numero} é {triplo}')
    print(f'O quadrado de {numero} é {quadrado}')
# ----------------------------------------------------------------------------------



# Se não sabemo quantas vezes precisaremos fazer isso, sem usar while True?
resposta = 'S'
while resposta == 'S':  # resposta != 'N'
    numero = int(input('\nDigite um número: '))
    dobro = numero * 2
    triplo = numero * 3
    quadrado = numero ** 2

    print(f'O dobro de {numero} é {dobro}')
    print(f'O triplo de {numero} é {triplo}')
    print(f'O quadrado de {numero} é {quadrado}')
    
    resposta = input('\nQuer continuar? [S/N]: ').upper()
# ----------------------------------------------------------------------------------



# Se não sabemo quantas vezes precisaremos fazer isso, usando while True?
# usando while true
while True:
    numero = int(input('\nDigite um número: '))

    if numero != 0:  
        # Se, só puder positivos maiores que 0 (if numero > 0)
        dobro = numero * 2
        triplo = numero * 3
        quadrado = numero ** 2

        print(f'O dobro de {numero} é {dobro}')
        print(f'O triplo de {numero} é {triplo}')
        print(f'O quadrado de {numero} é {quadrado}')
    else:
        print('Você digitou zero!')

    resposta = input('\nQuer continuar? [S/N]: ').upper()
    if resposta == 'N':
        break
# ----------------------------------------------------------------------------------

