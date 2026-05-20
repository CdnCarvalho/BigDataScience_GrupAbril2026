# ############### WHILE TRUE ####################

# FUNÇÃO → apenas calcula e retorna o IMC
def calcula_imc(p, a):
    imc = p / (a ** 2)
    return imc


# PROGRAMA PRINCIPAL
while True:

    print('\nNOVO CÁLCULO DE IMC')

    try:
        # ENTRADA DE DADOS
        peso = float(input('Informe o peso: '))
        altura = float(input('Informe a altura: '))

        # calcula o IMC
        imc = calcula_imc(peso, altura)


    except ValueError:
        # Caso o usuário digite letras ou caracteres especiais
        print('\nErro: Digite apenas números.')

        # continue


    except ZeroDivisionError:
        # Caso a altura seja zero
        print('\nErro: A altura não pode ser zero.')

        # continue


    else:
        # CLASSIFICAÇÃO com match/case
        match imc:

            case imc if imc < 17:
                classificacao = 'Muito abaixo do peso'

            case imc if imc < 18.5:
                classificacao = 'Abaixo do peso'

            case imc if imc < 25:
                classificacao = 'Peso normal'

            case imc if imc < 30:
                classificacao = 'Acima do peso'

            case imc if imc < 35:
                classificacao = 'Obesidade grau 1'

            case imc if imc < 40:
                classificacao = 'Obesidade grau 2'

            case _:
                classificacao = 'Obesidade grau 3'


        # EXIBIÇÃO
        print('\nRESULTADO:')
        print(30 * '=')

        print(f'IMC: {imc:.2f}')
        print(f'Classificação: {classificacao}')


    finally:
        # Sempre executa
        print('\nCálculo finalizado.')


    # CONTROLE DE SAÍDA
    continuar = input('\nDeseja continuar? (S/N): ').strip().upper()

    # Só NÃO entra no if, se continuar for igual a 'S'
    if continuar != 'S':
        break


print('\nPrograma encerrado.')