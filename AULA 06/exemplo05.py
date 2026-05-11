# lista para armazenar os dicionários dos vendedores
vendedores = []

# repetição para cadastrar 3 vendedores
for i in range(3):

    print(f"\nVENDEDOR {i+1}")

    # nome do vendedor
    nome = input("Digite o nome do vendedor: ")

    # lista para armazenar as vendas
    vendas = []

    # repetição sem quantidade definida
    while True:

        # solicita o valor da venda
        valor = float(input("Digite o valor da venda R$: "))
        vendas.append(valor)

        # pergunta se deseja continuar
        continuar = input("Deseja adicionar outra venda? [S/N]: ").strip().upper()[0]

        # encerra o while
        if continuar == "N":
            break

    # cálculos
    total = sum(vendas)
    media = total / len(vendas)

    # dicionário do vendedor
    vendedor = {
        "nome": nome,
        "vendas": vendas,
        "total": total,
        "media": media
    }

    # adiciona o dicionário na lista
    vendedores.append(vendedor)

# metas
META = 1000
META_MINIMA = 700

print("\nRESULTADOS")

# percorre a lista de dicionários
for vendedor in vendedores:

    print(f"\nVendedor: {vendedor['nome']}")
    print(f"Vendas: {vendedor['vendas']}")
    print(f"Total vendido: R$ {vendedor['total']:.2f}")
    print(f"Média das vendas: R$ {vendedor['media']:.2f}")

    # verificação das metas
    if vendedor["media"] >= META:
        print(f"Meta de R$ {META} atingida.")

    elif vendedor["media"] >= META_MINIMA:
        print(f"Bateu a meta mínima de R$ {META_MINIMA}.")

    else:
        print("Abaixo das metas.")