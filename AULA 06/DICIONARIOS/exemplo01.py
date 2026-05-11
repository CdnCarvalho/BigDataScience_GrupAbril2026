# ------------------------------------------------------------------------
# dicionario = {}  #-----  Cria vazio
# dicionario["chave"] = valor  #-----  Adiciona/Modifica
# print(dicionario["chave"])  #-----  Acessa valor
# del dicionario["chave"]  #-----  Remove item
# dicionario.clear()  #-----  Limpa tudo dentro do dicionário
# ------------------------------------------------------------------------

# criando um dicionário com produtos e seus respectivos preços
produto = {
    'nome': 'Notebook',
    'preco': 3500,
    'marca': 'Lenovo',
    'tela': '15.6'
}

print(produto)  # mostrando o dicionário


print(produto["nome"])  # acessando uma chave específica

produto["preco"] = 4000.0  # alterando o valor de uma chave

produto["processador"] = "Intel"  # adicionando uma nova informação

del produto["tela"]  # removendo uma informação

print(produto)
# -----------------------------------------------------------------------



# criando um dicionário com dados de uma pessoa
pessoa = {}

pessoa["nome"] = "João"
pessoa["idade"] = 25
pessoa["cidade"] = "Niterói"

print(pessoa)
# -----------------------------------------------------------------------



pessoa2 = {}
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")

pessoa2["nome"] = nome
pessoa2["idade"] = idade
pessoa2["cidade"] = cidade
# -----------------------------------------------------------------------
