# Crie um algoritmo que ecebe 4 notas por aluno e calcula a média de cada um. 
# As nostas são informadas pelo usuários.
# Como não sabemos a quantidade de alunos, o algoritmo pode perguntar se deseja continuar.


# Atividade 01 (versão 1)
# -------------------------------------------------------------------
# Resolvendo mais simples
c = 0
resposta = 'S'
while resposta != 'n':
    print(f'\nAluno {c}')
    c += 1
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    nota3 = float(input('Digite a nota 3: '))
    nota4 = float(input('Digite a nota 4: '))

    media = (nota1 + nota2 + nota3 + nota4) / 4 

    print(f'A média do {c}º aluno é: {media}')
    resposta = input('Deseja continuar? [S/N] ').lower()

print(f'\nForam computados {c} alunos')



# Atividade 01 (versão 2)
c = 0
resposta = 'S'
while resposta != 'n':
    print(f'\nAluno {c}')
    c += 1
    soma = 0    
    for i in range(1, 5):
        nota = float(input(f'Digite a nota{i}: '))
        soma += nota
    
    media = soma / 4
    
    print(f'A média do aluno {c} é: {media}')
    resposta = input('Deseja continuar? [S/N] ').lower()

print(f'\nForam computados {c} alunos')
# -------------------------------------------------------------------



# Atividade EXTRA
# Crie um Algoritmo que recebe valores de vendas (não sabemos o quanto) e calcule 
# o desconto de 10% para vendas acima de R$ 1000,00.
# O programa deve parar quando a resposta for N.

c = 0
resposta = 'S'
while resposta != 'N':
    c += 1
    valor = float(input(f'Digite o valor da {c}º venda: '))
    if valor > 1000:
        desconto = valor * 0.1
        valor -= desconto
    print(f'O valor da {c}º venda é: {valor}')

    resposta = input('Deseja continuar? [S/N] ').upper()
# -------------------------------------------------------------------

