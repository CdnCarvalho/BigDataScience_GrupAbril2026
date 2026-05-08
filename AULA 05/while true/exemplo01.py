# While True

# Exemplo 01
# Contar até 10
i = 0
while True:    
    if i > 10:
        break
    
    print(f'{i}', end=' ')
    i += 1


# Exemplo 02
# Somar números até digitar 0
soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    soma += n 

print(f'A soma é {soma}')


# Exemplo 03
# Calcular a média de notas e perguntar se deseja continuar
c = 0
while True:
    c += 1
    print(f'\n----- Aluno {c} -----')
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o primeiro número: "))
    
    total = n1 + n2
    print(f"Média: {total}")
    
    continuar = input("Deseja calcular outra média? (s/n): ").lower().strip()[0]
    print(continuar)
    
    if continuar == "n":
        break