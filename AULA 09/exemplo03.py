# ####### FUNÇÃO - cálculo da média
# Esta função recebe lista, 
# calcula o total das notas, a média, a maior e a menor
def calcular_media(lista_notas):
    tot = sum(lista_notas) # soma todas as notas
    med = tot / len(lista_notas)
    mai = max(lista_notas)
    men = min(lista_notas)
    return tot, med, mai, men  # retorna os dois valores



# PROGRAMA PRINCIPAL
contador = 1  # controle de alunos

while True:
    print(f'\nALUNO {contador}')
    print(30 * '=')

    # entrada de dados
    aluno = input('Informe o nome do aluno: ')

    notas = []  # lista para armazenar as 4 notas


    # coleta 4 notas usando for
    for i in range(4):
        nota = float(input(f'Informe a nota {i+1}: '))
        notas.append(nota)  # adiciona a nota na lista


    # chamada da função - enviamos a lista de notas p/ a função
    total, media, maior, menor = calcular_media(notas)

    # saída de dados
    print('\nRESULTADO:')
    print(f'Aluno: {aluno}')
    print(f'Soma das notas: {total:.2f}')
    print(f'Média final: {media:.2f}')
    print(f'Notas informadas: {notas}')  # Exibe todas as notas
    print(f'Maior nota: {max(notas):.2f}')  # maior
    print(f'Menor nota: {min(notas):.2f}')  # menor nota


    # pergunta se deseja continuar
    opcao = input('\nDeseja cadastrar outro aluno? (S/N): ').strip().upper()

    if opcao != 'S':
        break

    contador += 1

print('\nPrograma encerrado.')