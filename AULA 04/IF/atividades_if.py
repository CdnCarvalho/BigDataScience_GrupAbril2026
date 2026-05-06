# ======================================
# ####### ATIVIDADE 01 - Cálculo de bônus
# ENTRADA DE DADOS
salario = float(input('Informe o salário: R$ '))
venda = float(input('Informe o valor das vendas: R$ '))

# PROCESSAMENTO
# Verifica se a venda foi maior que 1000
if venda > 1000:
    # bonus = 100
    salario_final = salario + 100
else:
    # bonus = 20
    salario_final = salario + 20


# SAÍDA
print('\nRESULTADO')
print(f'Salário inicial: R$ {salario:.2f}')
print(f'Bônus recebido: R$ {(salario_final - salario):.2f}')
print(f'Salário final: R$ {salario_final:.2f}')
# -----------------------------------------------------------




# ATIVIDADE 02
# Entrada dos dados
valor = float(input("Informe o valor da compra: R$ "))
forma_pagamento = input("Informe a forma de pagamento (à vista ou parcelado): ").strip()

# Padronizando o texto para evitar erro de digitação
forma_pagamento = forma_pagamento.upper()

# Verificação das duas condições ao mesmo tempo
if valor > 250 and forma_pagamento == "PIX":
    desconto = valor * 0.16
    valor_final = valor - desconto
    print(f"Desconto de 16% aplicado. Valor final: R$ {valor_final:.2f}")
else:
    print(f"Sem desconto. Valor a pagar: R$ {valor:.2f}")
# --------------------------------------------------------------------------