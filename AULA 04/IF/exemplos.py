#  introdução ---------------------------
# se o tempo de casa for maior ou igual a 5 anos printa recebe bônus
tempo_casa = int(input('Informe o tempo de casa: '))
if tempo_casa >= 5:
    print('Recebe bônus')
else:
    print('Não recebe bônus')
# ----------------------------------------



# EXEMPLO 1 - Consumo de combustível
# Enunciado: Verifique se o consumo do carro é econômico ou não
distancia = float(input('Informe a distância percorrida (km): '))
combustivel = float(input('Informe o combustível gasto (litros): '))

# cálculo do consumo (km por litro)
consumo = distancia / combustivel

# decisão
if consumo >= 12:
    print(f'Veículo econômico! Consumo: {consumo:.2f} km/l')
else:
    print(f'Veículo não é econômico. Consumo: {consumo:.2f} km/l')

# -------------------------------------------------------------------
# Atividade 01


# EXEMPLO 2 - Aumento por setor
# ENTRADA DE DADOS
salario = float(input('Informe o salário: R$ '))
tempo = int(input('Informe o tempo de empresa (anos): '))
setor = input('Informe o setor do funcionário: ').strip().upper()

# PROCESSAMENTO
# Agora usamos duas condições com AND
if setor == 'A' and tempo > 3:
    aumento = salario * 0.18
    novo_salario = salario + aumento
else:
    aumento = salario * 0.09
    novo_salario = salario + aumento

# novo_salario = salario + aumento

# SAÍDA
print('\nRESULTADO')
print(f'Aumento: R$ {aumento:.2f}')
print(f'Novo salário: R$ {novo_salario:.2f}')
# ------------------------------------------------------------------
# Atividade 02



# Se precisar de mais um ir direto para o exemplo de ifs encadeado






############### IFS ENCADEADOS ##############
# EXEMPLO 6 - IF dentro de IF (aninhado)
# Enunciado: Verifique se o aluno passou de ano e se teve boa frequência.
nota = float(input("Digite a média final do aluno: "))
frequencia = float(input("Digite a frequência do aluno (em %): "))

# Verifica se o aluno passou por nota
if nota >= 7:
    # Aluno passou por nota
    # Precisa verificar a frequência
    if frequencia >= 75:
        print("Aluno aprovado com bom desempenho e boa frequência.")
    else:
        print("Aluno com boa nota, mas reprovado por falta.")
else:
    # if frequencia >= 75:
    #     print("Aluno com boa frequência, mas reprovado por nota baixa.")
    # else:
    #     print("Aluno reprovado por nota baixa e falta.")
    print("Aluno reprovado por nota baixa.")
# -----------------------------------------------------------


# EXEMPLO 7 - IF dentro de IF (aninhado com alternativa no ELSE)
# Enunciado: Verifique se o cliente pode parcelar a compra e qual será o número máximo de parcelas.
valor_compra = float(input("Digite o valor total da compra: "))

if valor_compra >= 100:
    print("Compra elegível para parcelamento.")
    if valor_compra > 1000:
        parcela = valor_compra / 10
        print(f"Você pode parcelar em até 10x de R$ {parcela} sem juros.")
    elif valor_compra > 700:
        parcela = valor_compra / 5
        print(f"Você pode parcelar em até 5x de R$ {parcela} sem juros.")
    else:
        parcela = valor_compra / 3
        print(f"Você pode parcelar em até 3x de R$ {parcela} sem juros.")
        
else:
    print(f"Valor abaixo do mínimo para parcelamento. \nPagamento à vista: R$ {valor_compra}.")
# -----------------------------------------------------------
