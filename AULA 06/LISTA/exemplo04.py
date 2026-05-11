# lista para armazenar 
media_vendas = []
total_vendas = []

for i in range(10):
    print(f"\nVENDEDOR {i+1}")

    qtd = int(input("Quantidade de vendas: "))

    vendas = []   # lista para armazenar as vendas do vendedor atual

    # cadastrando as vendas
    for n in range(qtd):
        valor = float(input(f"Digite o valor da venda{n+1} R$: "))
        vendas.append(valor)

    # calculando as vendas
    total = sum(vendas)
    media = total / qtd

    # armazenando os resultados
    total_vendas.append(total)
    media_vendas.append(media)



# definição das metas
META = 1000
META_MINIMA = 700

print('\nRESULTADOS')
# Analisando os resultados
for i, media in enumerate(media_vendas):
    print(f"\nVendedor {i+1}")
    print(f"Total vendido: R$ {total_vendas[i]:.2f}")
    print(f"Média das vendas: R$ {media:.2f}")

    if media >= META:
        print(f"Meta de R$ {META} atingida.")

    elif media >= META_MINIMA:
        print(f"Bateu a meta mínima de R$ {META_MINIMA}.")

    else:
        print("Abaixo das metas.")



# Versão 2 - while true
# ------------------------------------------------------------------------------------
# lista para armazenar as médias
media_vendas = []
total_vendas = []

for i in range(3):

    print(f"\nVENDEDOR {i+1}")

    # lista para armazenar as vendas do vendedor atual
    vendas = []

    # repetição sem quantidade definida
    while True:
        valor = float(input("Digite o valor da venda R$: "))
        vendas.append(valor)

        # pergunta se existem mais vendas
        continuar = input("Deseja adicionar outra venda? [S/N]: ").strip().upper()[0]

        # encerra o while se a resposta for N
        if continuar == "N":
            break

    # calculando os resultados
    total = sum(vendas)
    media = total / len(vendas)

    # armazenando os resultados
    total_vendas.append(total)
    media_vendas.append(media)

# definição das metas
META = 1000
META_MINIMA = 700

print('\nRESULTADOS')

# analisando os resultados
for i, media in enumerate(media_vendas):

    print(f"\nVendedor {i+1}")
    print(f"Total vendido: R$ {total_vendas[i]:.2f}")
    print(f"Média das vendas: R$ {media:.2f}")

    if media >= META:
        print(f"Meta de R$ {META} atingida.")

    elif media >= META_MINIMA:
        print(f"Bateu a meta mínima de R$ {META_MINIMA}.")

    else:
        print("Abaixo das metas.")



