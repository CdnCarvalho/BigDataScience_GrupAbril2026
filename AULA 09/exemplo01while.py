# ##### EXEMPLO 02
def dobro(n):
    return n * 2


def triplo(n): 
    return n * 3


def quadrado(n):
    return n ** 2


def metade(n):
    return n / 2



# Algoritmo que usuário informa dois números e escolhe se quer o dobro, ou triplo, ou o quadrado 
# calcular a metade
while True:
    
    n = int(input('\nInforme o número: '))

    print('\n ###### MENU DE OPÇÕES ######')
    print(30*'=')
    print('[0] - Sair\n[1] - Metade\n[2] - Dobro\n[3] - Triplo - \n[4] - Quadrado')
    
    opcao = int(input('\nDigite a opção desejada: '))    
    resposta = False  # Ensinar com None recomendado

    match opcao:
        case 0:
            pass
        case 1:
            resposta = metade(n)
        case 2:
            resposta = dobro(n)
        case 3:
            resposta = triplo(n)
        case 4:
            resposta = quadrado(n)  # pedir depois
        case _:
            resposta = 'Opção inválida'


    # if resposta is not None:  Opção melhor
    # if resposta is not False:  Opção boa
    if resposta != False:  # não recomendável. Gera erro se o número for 0
        print(f'Resultado: {resposta}')
        # pedir para dar mais uma opção: calcular a metade
    else:
        print('Finalizando o programa...')
 
    # Encerrando o programa
    if opcao == 0:
        break

print('Fim do programa')