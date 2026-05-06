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