# usando o for para percorrer a lista
lista_produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor']


for i in range(4):
    # elemento = lista_produtos[i]
    print(i)
    print(lista_produtos[i])



for produto in lista_produtos:
    print(produto)


# Quando precisar ler a posição do elemento
for i, p in enumerate(lista_produtos):
    print(i, p)

