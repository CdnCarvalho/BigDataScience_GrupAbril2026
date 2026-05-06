# Mat Case - Estrutura de controle de fluxo para múltiplas condições
# Usado para substituir múltiplos IFs encadeados, tornando o código mais legível e organizado.

# EXEMPLO 01
# Recebe o código de acesso digitado pelo usuário
# e imprime a área correspondente usando match/case
# Se o código for 1, exibe "Marketing"
# Se o código for 2, exibe "Financeiro"
# Se o código for 3, 4 ou 5, exibe "ADM"
# Se o código for 6, 7, 8 ou 9, exibe "TI"
# Se o código for 10 a, exibe "Serviços Gerais"

# EXEMPLO 01.2 (Substituindo o Pipe pelo if e Operador Or)
# Recebe o código de acesso digitado pelo usuário
print("""
[1] - Marketing
[2] - Financeiro
[3 a 5] - ADM
[6 a 9] - TI
[10 a 20] - Serviços Gerais
""")
codigo = int(input("Informe o código de acesso: "))

# Verifica a área correspondente com base no código usando match/case
match codigo:
    case 1:
        print("Marketing")
    case 2:
        print("Financeiro")
    case codigo if codigo == 3 or codigo == 4 or codigo == 5:
        print("ADM")
    case 6 | 7 | 8 | 9:  # Usando o Pipe | no sentido de 6 ou 7
        print("TI")
    case numero if 10 <= numero <= 20:  # # Lê-se: "caso numero, se 10 for menor ou igual a numero "E" numero for menor ou igual a 20"
        print("Serviços Gerais")
    case _:
        print("Acesso negado.")
# -------------------------------------------------------------------------



# --------------------------------------------------------
###### Exemplo 2
# Classificando idade
# Anunciado: Verificar a faixa etária está entre os intervalos:
# 0 a 11 anos = Criança
# 12 a 17 anos = Adolescente
# 18 anos ou mais = Adulto
print("""
CLASSIFICAÇÃO POR IDADE:
ADULTO: 18 anos ou mais
ADOLESCENTE: 12 a 17 anos
CRIANÇA: 11 anos ou menos
""")

idade = int(input("Digite a idade: "))

match idade:
    case i if 0 <= i < 12:
        print("Criança")
    case i if 12 <= i < 18:
        print("Adolescente")
    case i if i >= 18:
        print("Adulto")
    case _:
        print("Idade inválida.")


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

opcao = input("Escolha a opção: ")

# Variável de controle
desconto = 0

match opcao:
    case "1":
        desconto = valor * 0.12
        print("\n--- Pagamento via PIX ---")

    case "2":
        desconto = valor * 0.08
        print("\n--- Pagamento no Débito ---")

    case "3":
        desconto = valor * 0.05
        print("\n--- Pagamento no Crédito ---")

    case "4":
        desconto = valor * 0.15
        print("\n--- Pagamento em Dinheiro ---")

    case _:
        print("\nOpção inválida.")


#  Se o desconto for diferente de zero, calcula o valor final e exibe os detalhes do pagamento. 
#  Isso indica que o usuário escolheu uma opção válida (1 a 4) e o desconto foi aplicado, atribuindo
#  um novo valor à variável "desconto". "A variável desconto não é mais o valor Zero"
 
#  Se o desconto for zero, quer dizer que a opção escolhida acima pelo usuário, não corresponde a nenhuma das 
#  formas de pagamento listadas. Então, neste caso, esta condição será Falsa o fluxo será direcionado para o Else.
if desconto != 0:
    valor_final = valor - desconto
    print(f"Preço normal: R$ {valor:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Preço final: R$ {valor_final:.2f}")
else:
    print('Escolha uma das opções informadas acima.')
# ---------------------------------------------------------------------


