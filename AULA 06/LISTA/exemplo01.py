# Lista
list_mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho"]

# exibir a lista
print(list_mes)

# exibir primeiro item da lista
print(list_mes[0])

# exibir o último item da lista
print(list_mes[-1])

# exibir o penúltimo item da lista, configure-a com [-2], 
# caso queira o antepenúltimo, use [-3] etc
print(list_mes[-2])

# exibir um índice específico
print(list_mes[3])

# exibir somente um parte da lista 1 a 3
print(list_mes[1:4])

# exibir do índice 2 até o final
print(list_mes[2:])

# exibir a partir do índice 0 até o índice do 3, que é o 4-1
print(list_mes[:4])

# exibir do índice 0 até 6-1, indo de dois em dois
print(list_mes[0:6:2])


# Usando For para ler a iterar por cada elemento da lista
# Desta forma podemos manipular os dados de uma lista, realizando operações
# cada elemento separadamente.
# No nosso exemplo, estaremos apenas exibindo os dados da lista.
for m in list_mes:
    print(m)