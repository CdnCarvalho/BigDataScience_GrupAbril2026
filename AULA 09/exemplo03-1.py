# ####### FUNÇÕES ESPECIALISTAS
def calcular_nota(lista_notas):
    """Calcula estritamente a soma e a média."""
    tot = sum(lista_notas)
    med = tot / len(lista_notas)
    return tot, med


def mostrar_resultado(a, tot, med):
    """Exibe os dados formatados na tela."""
    print(f'\nAluno: {a}')
    print(f'Total: {tot:.1f}')
    print(f'Média: {med:.1f}')



# ####### FUNÇÃO ORQUESTRADORA
def processar_boletim(a, lista_notas):
    """Centraliza o fluxo: valida, calcula e mostra o resultado."""
    

    # Varremos a lista de notas para verificar se há notas negativas
    for nota in lista_notas:
        if nota < 0:
            print(f'\n[ERRO] {aluno} possui nota negativa ({nota}).')
            print('O boletim não pôde ser gerado.')
            return  # O return encerra a função e volta para o loop.
    

    # Se o código passou pelo 'for' sem entrar no 'return', ele executa as chamadas:
    total_notas, media_notas = calcular_nota(lista_notas) 
    

    # Passamos o resultado da primeira diretamente para a segunda
    mostrar_resultado(aluno, total_notas, media_notas)




# PROGRAMA PRINCIPAL
contador = 1

while True:
    print()
    print(f'ALUNO {contador}')
    print(30 * '-')


    aluno = input('Informe o nome do aluno: ')
    notas = []  


    for i in range(4):
        nota = float(input(f'Informe a nota {i+1}: '))        
        notas.append(nota)


    # CHAMADA ÚNICA: Delegamos tudo para a função orquestradora
    processar_boletim(aluno, notas)


    opcao = input('\nDeseja cadastrar outro aluno? (S/N): ').strip().upper()
    if opcao != 'S':
        break

    contador += 1

print('\nPrograma encerrado.')