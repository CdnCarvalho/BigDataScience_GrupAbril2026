# Atividade 01
# repete o cadastro para 5 pessoas
for pessoa in range(5):

    print(f"\n---- Pessoa {pessoa + 1} ----")

    # entrada das compras
    compra1 = float(input("Digite o valor da primeira compra: R$ "))
    compra2 = float(input("Digite o valor da segunda compra: R$ "))

    # cálculo do total gasto
    total_gasto = compra1 + compra2

    # saída de dados
    print(f"Total gasto pela pessoa {pessoa + 1}: R$ {total_gasto:.2f}")
# ---------------------------------------------------------------------------------




# Atividade 02
# # repete o cadastro de vendedores 5 vezes
for i in range(5):

    print(f"\nVendedor {i+1}")

    # entrada de dados
    vendas = float(input("Digite o valor das vendas: R$ "))
    salario = float(input("Digite o salário do vendedor: R$ "))

    # verifica se atingiu a meta
    if vendas >= 5000:
        bonus = salario * 0.04
    else:
        bonus = 0

    # cálculo do total a receber
    total = salario + bonus

    # saída de dados
    print(f"Bônus recebido: R$ {bonus:.2f}")
    print(f"Total a receber: R$ {total:.2f}")



# Versão 2 (versão 1)
# repete para 5 vendedores
for i in range(5):

    print(f"\nVendedor {i+1}")

    # entrada do salário
    salario = float(input("Digite o salário do vendedor: R$ "))

    # variável acumuladora das vendas
    total_vendas = 0

    # controle de repetição
    continuar = "s"

    # recebe várias vendas
    while continuar == "s":

        venda = float(input("Digite o valor da venda: R$ "))

        # soma as vendas
        total_vendas += venda

        # pergunta se deseja continuar
        continuar = input("Deseja cadastrar outra venda? (s/n): ").lower()

    # verifica se atingiu a meta
    if total_vendas >= 5000:
        bonus = salario * 0.04
    else:
        bonus = 0

    # cálculo do total a receber
    total_receber = salario + bonus

    # saída de dados
    print(f"\nTotal de vendas: R$ {total_vendas:.2f}")
    print(f"Bônus recebido: R$ {bonus:.2f}")
    print(f"Total a receber: R$ {total_receber:.2f}")
# ---------------------------------------------------------------------------------