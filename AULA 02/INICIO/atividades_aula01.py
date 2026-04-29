
# ATIVIDADE 1
# 01 - Elabore um programa que imprima na tela a seguinte 
# frase `Análise de Dados em Python`
# -------------------------------------------------------------------------------------


# 02 - Elabore um programa que escreve seu nome completo de uma pessoa na primeira linha, 
# o bairro na segunda e o CEP e telefone na terceira.  

# EXEMMPLO
# Nome: Bruno Fabri
# Endereço: Rua ABC
# CEP: 002220-010
# 
# -------------------------------------------------------------------------------------



# 03 - Elabore um programa que recebe o nome de uma pessoa do terminal e mostra 
# a seguinte mensagem: `Olá {nome}! Seja bem vindo ao fantástico mundo da programação`
# -------------------------------------------------------------------------------------



# ATIVIDADE 1
# 1. Crie um programa que leia um número e mostre o seu anterior e o seu sucessor.
# E mostre-os no final.
num = int(input("Digite um número: "))
anterior = num - 1
sucessor = num + 1
print(f"O número anterior é {anterior}")
print(f"E o sucessor é {sucessor}")
# --------------------------------------------------------------------------------------



# ATIVIDADE 2
# 1. Crie um programa que leia um número e mostre seu dobro, triplo e o quadrado.
num = int(input("Digite um número: "))
dobro = num * 2
triplo = num * 3
quadrado = num ** 2
print(f"O dobro de {num} é {dobro}")
print(f"O triplo de {num} é {triplo}")
print(f"O quadrado de {num} é {quadrado}")
# --------------------------------------------------------------------------------------



# ATIVIDADE 3
# Enunciado: Descubra quantos ingressos de cinema podem ser comprados com o valor disponível.
preco_unitario = float(input("Digite o preço de um ingresso de cinema: "))
valor_disponivel = float(input("Digite quanto dinheiro você tem para a compra: "))
quantidade = float(valor_disponivel // preco_unitario)
troco = float(valor_disponivel % preco_unitario)
print(f"Com R$ {valor_disponivel}, você pode comprar {quantidade}, ingresso(s). O troco é R$ {troco:.2f}")
# ------------------------------------------------------------



# ATIVIDADE 4 - Aumento de salário
# Enunciado: Calcule o novo salário de um funcionário com aumento de 15%.
salario = float(input("Digite o valor do seu salário: "))
aumento = salario * 0.15
novo_salario = salario + aumento
print("Seu novo salário com aumento é:", novo_salario)





#  ############### ATIVIDADES PDT #################

# ATIVIDADE 1 — Boletim escolar
# Criar duas variáveis com as notas
nota1 = 6.0
nota2 = 9.0

# Calcular a média e guardar em uma terceira variável
media = (nota1 + nota2) / 2

print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Média:", media)



# ATIVIDADE 2 — Calculadora com input
# Receber dois números do usuário
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

# Calcular e guardar as operações
soma      = n1 + n2
subtracao = n1 - n2
produto   = n1 * n2
divisao   = n1 / n2
modulo    = n1 % n2

# Exibir os resultados
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", produto)
print("Divisão:", divisao)
print("Módulo:", modulo)



