# COMANDO FOR 
# ---------------------------------------------------------------------------------------
# EXEMPLOS PRÁTICOS - ESTRUTURA DE REPETIÇÃO FOR
# ----------------------------------------------------------------------------------------

# Exemplo 1 – Repetição simples com mensagem
for n in range(5):  # repete o bloco abaixo 5 vezes (valores de 0 até 4)
    print("olá mundo")  # exibe a mensagem "olá mundo" a cada repetição

# ----------------------------------------------------------------------------------------


# Exemplo 2 – Contando de 0 até 4
for n in range(10):  # n vai assumir os valores 0, 1, 2, 3 e 4
    print(n)  # mostra o valor atual de n

# ----------------------------------------------------------------------------------------


# Exemplo 6 – Soma 3 pares de números (Usuário informa dois números a cada iteração)
for n in range(3):  # repete o bloco 3 vezes 
    n1 = float(input("Informe o primeiro número: "))  # recebe o nome da pessoa
    n2 = float(input("Informe o segundo número: "))  # recebe o nome da pessoa
    soma = n1 + n2
    print(f'Resultado: {soma}')  

# ----------------------------------------------------------------------------------------
