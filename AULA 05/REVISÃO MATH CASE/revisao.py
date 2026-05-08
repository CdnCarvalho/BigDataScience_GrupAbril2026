# Mat Case - Estrutura de controle de fluxo para múltiplas condições

# --------------------------------------------------------
###### Exemplo 1  (versao 1)
# Classificando idade
# Anunciado: Verificar a faixa etária está entre os intervalos:
# 0 a 11 anos = Criança
# 12 a 17 anos = Adolescente
# 18 anos ou mais = Adulto

print("""
[1] - CRIANÇA
[2] - ADOLESCENTE
[3] - ADULTO
""")

opcao = float(input("Escolha uma opção: "))

match opcao:
    case op if 0 <= op < 12:  # i <= i < 12
        print("Criança")
    case op if 12 <= op < 18: # 12 <= i < 18
        print("Adolescente")
    case op if op >= 18:
        print("Adulto")
    case _:
        print("Idade inválida.")



# ###### Exemplo 1 (versão 2)
print("""
CLASSIFICAÇÃO POR IDADE:
ADULTO: 18 anos ou mais
ADOLESCENTE: 12 a 17 anos
CRIANÇA: 11 anos ou menos
""")

idade = float(input("Digite a idade: "))

match idade:
    case i if 0 <= i < 12:  # i <= i < 12
        print("Criança")
    case i if 12 <= i < 18: # 12 <= i < 18
        print("Adolescente")
    case i if i >= 18:
        print("Adulto")
    case _:
        print("Idade inválida.")
# --------------------------------------------------------



# --------------------------------------------------------
###### ATIVIDADE 1
# Enunciado: Verificar se um número é positivo, negativo ou zero.
# O programa deve receber um número informado pelo usuário e usar 
# match/case para classifica-lo em positivo, negativo, ou zero.

num = float(input("Digite um número: "))

# Verifica se o número é positivo, negativo ou zero
match num:
    case num if num > 0:
        print(f"{num} é positivo")
    case num if num < 0:
        print(f"{num} é negativo")
    case 0:
        print(f"{num} Zero é neutro")


# --------------------------------------------------------
###### Atividade 2
valor = float(input("Digite um valor de venda: "))

bonus = 0
opcao_valida = True

match valor:
    case v if 0 <= v < 100:
        print("Sem Bônus")

    case v if 100 <= v < 500:
        bonus = valor * 0.05
        print("Bônus de 5%")

    case v if v >= 500:
        bonus = valor * 0.10
        print("Bônus de 10%")

    case _:
        print("Valor inválido")
        opcao_valida = False


# cálculo e saída fora do match
if opcao_valida:
    valor_final = valor + bonus
    print(f"Bônus: R$ {bonus:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")
# --------------------------------------------------------



####### EXEMPLO 3 - Match Case e If
# Enunciado: Criar um sistema de pagamento, que oferece diferentes descontos
# com base na forma de pagamento escolhida pelo usuário.
# O programa recebe o valor da compra e a forma de pagamento escolhida
# pelo usuário e usa o match/case para aplicar o desconto correspondente.

# As formas de pagamento disponíveis são: 
# Pix (12% de desconto) 
# Débito (8% de desconto)
# Crédito (5% de desconto)
# Dinheiro (15% de desconto)

valor = float(input("Informe o valor da compra: R$ "))

# Menu de formas de pagamento
print("""
FORMAS DE PAGAMENTO
1 - Pix  (12% de desconto)
2 - Débito  (8% de desconto)
3 - Crédito  (5% de desconto)
4 - Dinheiro  (15% de desconto)
""")

opcao = int(input("Escolha a opção: "))

# Variável de controle
desconto = 0

match opcao:
    case 1:
        desconto = valor * 0.12
        print("\n--- Pagamento via PIX ---")

    case 2:
        desconto = valor * 0.08
        print("\n--- Pagamento no Débito ---")

    case 3:
        desconto = valor * 0.05
        print("\n--- Pagamento no Crédito ---")

    case 4:
        desconto = valor * 0.15
        print("\n--- Pagamento em Dinheiro ---")

    case _:
        print("\nOpção inválida.")


#  Se o desconto for diferente de zero, calcula o valor final e exibe os detalhes do pagamento. 
#  Isso indica que o usuário escolheu uma opção válida (1 a 4) e o desconto foi aplicado, atribuindo
#  um novo valor à variável "desconto". "A variável desconto não é mais o valor Zero"
 
#  Se o desconto for zero, quer dizer que a opção escolhida acima pelo usuário, não corresponde a nenhuma das 
#  formas de pagamento listadas. Então, neste caso, esta condição será Falsa o fluxo será direcionado para o Else.
# if desconto != 0:
if opcao in [1, 2, 3, 4]:
    valor_final = valor - desconto
    print(f"Preço normal: R$ {valor:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Preço final: R$ {valor_final:.2f}")
else:
    print('Escolha uma das opções informadas acima.')
# ---------------------------------------------------------------------


