# EXEMPLO 1 - IF / ELSE básico
# Enunciado: Verifique se a pessoa é maior de idade.
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
# -----------------------------------------------------------


# EXEMPLO 1.1 - IF com ELIF
# Enunciado: Verifique a faixa de pontuação de um jogador.
pontos = int(input("Digite sua pontuação: "))

if pontos >= 100:
    total = pontos + 10
    print(f"Excelente! Bônus adicionado. Agora você tem {total} pontos.")
elif pontos >= 50:
    total = pontos + 5
    print(f"Bom desempenho! Bônus adicionado. Agora você tem {total} pontos.")
else:
    print(f"Você está começando, pratique mais! Sua pontuação foi de: {pontos}")
# -----------------------------------------------------------
# >>>>>>> Atividade 01



# EXEMPLO 2 - IF com operador AND
# Enunciado: Verifique se o usuário pode realizar o login.
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Login realizado com sucesso.")
else:
    print("Usuário ou senha incorretos.")
# -----------------------------------------------------------


# EXEMPLO 3 - Combinação de condições com AND e OR
# Enunciado: Verifique se o cliente tem direito a um brinde.
compra = float(input("Digite o valor da compra: "))
cliente_frequente = input("O cliente é cadastrado no programa de fidelidade? (s/n): ").strip().lower()[0]
print(cliente_frequente)
if compra > 100 or cliente_frequente == "s":
    print("Cliente tem direito a um brinde!")
else:
    print("Sem brinde desta vez.")
# -----------------------------------------------------------
# >>>>>>> Atividade 02



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
