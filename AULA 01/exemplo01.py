# BLOCO 1 — O que é uma variável?
# "Uma variável é como uma caixinha com nome. Você guarda um valor dentro dela e 
# pode usar esse valor depois."
# Criando variáveis e associando valores

nome = "Ana"
idade = 17
altura = 1.65
aprovado = True

print(nome)
print(idade)
print(altura)
print(aprovado)
# -----------------------------------------------------------------------------------



# BLOCO 2 — Tipos de variáveis
# "Python identifica automaticamente o tipo pelo valor que você coloca.
#  Vamos ver os tipos mais comuns."
# int → número inteiro
quantidade = 10

# str → texto (string)
produto = "olá"


# float → número com casas decimais
preco = 4.99


# bool → verdadeiro ou falso
em_estoque = True

# Verificando o tipo de cada variável
print(type(quantidade))
print(type(preco))
print(type(produto))
print(type(em_estoque))
# -----------------------------------------------------------------------------------



#  BLOCO 3 — Operadores matemáticos
# Agora que sabemos guardar valores, vamos fazer contas com eles
a = 10
b = 3

soma        = a + b
subtracao   = a - b
multiplicao = a * b
divisao     = a / b
divisao_int = a // b   # divide e joga fora a parte decimal
modulo      = a % b    # resto da divisão
potencia    = a ** b   # a elevado a b

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicao)
print("Divisão:", divisao)
print("Divisão inteira:", divisao_int)
print("Módulo (resto):", modulo)
print("Potência:", potencia)
# -----------------------------------------------------------------------------------



#  BLOCO 4 — Acumulando resultado em variável
# "O resultado de um cálculo também pode ser guardado em uma variável nova."
nota1 = 7.5
nota2 = 8.0

media = (nota1 + nota2) / 2

print("Média:", media)
# -----------------------------------------------------------------------------------



# BLOCO 5 — Recebendo dados do usuário com input()
# "Até agora nós colocamos os valores no código. Mas e se quisermos que o usuário digite? 
# Usamos o input()." # input() sempre retorna texto (str)
nome = input("Digite seu nome: ")
print("Olá,", nome)


# Para usar em cálculos, precisamos converter para número
# primeiro sem o int(), rode, tente fazer numero * 2 e mostre o erro.
numero = input("Digite um número: ")
numero = int(numero)   # converte para inteiro
print("O dobro é:", numero * 2)
# -----------------------------------------------------------------------------------




# BLOCO 6 — int() vs float() no input
# Use int() para números inteiros
idade = int(input("Digite sua idade: "))

# Use float() para números com decimais
altura = float(input("Digite sua altura: "))

print("Daqui 5 anos você terá", idade + 5, "anos")
print("Sua altura em centímetros:", altura * 100)
# -----------------------------------------------------------------------------------