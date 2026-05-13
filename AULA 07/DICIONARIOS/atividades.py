# ATIVIDADE 01
# Lista para armazenar os contatos
contatos = []

# Cadastro de 5 contatos
for i in range(5):
    print(f"\nCadastro do {i+1}º contato:")

    # criação do dicionário vazio
    contato = {}

    # preenchimento dos dados
    contato['nome'] = input("Nome completo: ")
    contato['telefone'] = input("Telefone: ")
    contato['email'] = input("E-mail: ")

    # adiciona o contato na lista
    contatos.append(contato)

    print("Contato cadastrado com sucesso!")

# Exibe todos os contatos cadastrados
print("\n--- LISTA DE CONTATOS ---")

for c in contatos:
    print(c)

# --------------------------------------------------------------------------------


# ATIVIDADE 02 
# Vendas maior ou igual a Meta 5000
# Lista para armazenar os vendedores
vendedores = []

# Cadastro de 3 vendedores
for i in range(3):
    print(f"\nCadastro do {i+1}º vendedor:")

    vendedor = {}

    vendedor['nome'] = input("Nome: ")
    vendedor['regiao'] = input("Região: ")
    vendedor['vendas'] = float(input("Valor total de vendas no mês: "))
    vendedor['quantidade'] = int(input("Quantidade de vendas: "))

    vendedores.append(vendedor)
    print("Vendedor cadastrado com sucesso!")

# Mostra apenas vendedores que atingiram a meta
print("\n--- VENDEDORES QUE ATINGIRAM A META ---")
for vendedor in vendedores:
    if vendedor['vendas'] >= 5000:
        print(vendedor)




