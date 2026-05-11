# LISTA PARA ARMAZENAR 5 NÚMEROS
lista_produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor']

# Mostrando os dados
print(f"\nLista Inicial: {lista_produtos}")


# Iterando sobre os elementos da lista usando for. Aqui não precisamos do range()
for p in lista_produtos:
    print(p)


# A lista guarda vários elementos, cada um em uma posição,
# onde cada elemento terá um Índice, que identifica a posição dele na lista.
# Toda lista inicia com índice 0. Então o primeiro elemento sempre estará na posição 0 
# e o último elemento estará na posição (n-1), onde "n" significa o número total de elementos na lista.


# Alterando o primeiro elemento da lista
lista_produtos[0] = "PC Desktop"
print("Lista Alterada:", lista_produtos)

# Adicionando elemento
lista_produtos.append("Webcam")
print("Novo produto adicionado:", lista_produtos)

# Adicionando em um Índice
# Adicionando um produto novo no índice 2
lista_produtos.insert(2, "Headset")

# Removendo um produto
lista_produtos.remove("Monitor")  # só remove se o número existir
print("Lista após Remoção:", lista_produtos)

# Removendo o elemento da última posição
lista_produtos.pop()
print("Remoção do Último:", lista_produtos)

# Removendo um elemento pelo índice
del lista_produtos[0]
print("Lista Removendo pelo índice:", lista_produtos)

# Limpando a lista
#  Este comando apaga tudo que está na lista. A lista conitinua existindo, porém estará Vazia []
lista_produtos.clear()

# Exclui a lista inteira da execução do algoritmo, neste caso a lista deixa de existir
del lista_produtos

print(lista_produtos)

