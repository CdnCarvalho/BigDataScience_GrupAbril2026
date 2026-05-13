# ------------------------------------------------------------------------
# Dicinários - ARMAZENAR LIVROS E MOSTRAR SOMENTE OS LIVROS COM LANÇAMENTO APÓS 2020
# Forma Didático p/ entender como funciona

# Lista para armazenar os livros
livros = []

# Cadastro de 3 livros
for i in range(3):
    print(f"\nCadastro do {i+1}º livro:")

    livro = {}  # Um dicionário novo será criado todavez que o "laço FOR" for ser repetido

    livro['titulo'] = input("Título: ")
    livro['ano'] = int(input("Ano: "))
    livro['genero'] = input("Gênero: ")

    livros.append(livro)  # Cada dicionário será adicionado a lista, a cada repetição do laço FOR
    print("Livro cadastrado com sucesso!")


# Mostra apenas livros a partir de 2020
# A variável 'l' na estrutura de repetição FOR abaixo, itera por cada um dos elementos da lista, 
# A lista em questão, está armazenando vários dicionários. 
# Cada livro é um dicionário. Então a letra 'l' é um dicionário.
# Todo dicionário tem uma chave 'ano' que contém o ano de lançamento do livro.
print("\n--- LIVROS A PARTIR DE 2020 ---")
for l in livros:
    if l['ano'] >= 2020:
        print(l)  # Mostrar o dicionário inteiro
        
        # Mostrar o nome e o ano cada livor
        print(f"Nome do Livro: {l['titulo']} ")
        print(f"Ano de Publicação: {l['ano']} ")

# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# MESMO EXEMPLO ANTERIOR, PORÉM MUDANDO A FORMA COMO CRIAMOS O DICIONÁRIO - USO NO DIA A DIA

# Lista para armazenar os livros
livros = []

# Cadastro de 3 livros
for i in range(3):
    print(f"\nCadastro do {i+1}º livro:")

    # Primeiro recebemos os dados que serão armazenados no dicionário, com input() em variáveis simples
    titulo = input("Título: ")
    ano = int(input("Ano de publicação: "))
    genero = input("Gênero: ")


    # Criação do Dicionário:
    # Neste modo, não criamos um dicionário vaziom e sim um dicionário com os dados já inseridos.
    # Observe:
    # Pegamos os dados das variáveis simples e os colocamos após os ":" como valores das chaves do dicionário 
    # A chave 'titulo', obtém o valor da variável titulo, a chave 'autor' obtém o valor da variável autor, e assim por diante.
    # OBS: Abaixo, as palavras, sempre à esquerda e entre aspas são as chaves do dicionário. As outras são as variáveis simples.
    livro = {
        'titulo': titulo,
        'ano': ano,
        'genero': genero,
    }

    # Adiciona o dicionário à lista
    livros.append(livro)
    print("Livro cadastrado com sucesso!")

# Mostra apenas livros a partir de 2020
print("\n--- LIVROS A PARTIR DE 2020 ---")
for livro in livros:
    if livro['ano'] >= 2020:
        # print(livro)

        # Mostrar o nome e o ano
        print(f'O nome do livro: {livro['titulo']}')
        print(f'O ano de publicação foi {livro['ano']}')



# --------------------------------------------------------
# MESMO EXEMPLO ANTERIOR - FAZENDO O USO DO WHILE
# Empregamos aqui a FORMA DIDÁTICA na criação do dicionário

# Lista para armazenar os livros
livros = []
contador = 1

# Cadastro de livros
while True:
    print(f"\nCadastro do {contador}º livro:")

    livro = {}

    livro['titulo'] = input("Título: ")
    livro['ano'] = int(input("Ano de publicação: "))
    livro['genero'] = input("Gênero: ")

    livros.append(livro)
    print("Livro cadastrado com sucesso!")

    contador += 1

    # Pergunta se deseja continuar
    continuar = input("Deseja cadastrar outro livro? (s/n): ").lower()
    
    if continuar == "n":
        break

# Mostra apenas livros a partir de 2020
print("\n--- LIVROS A PARTIR DE 2020 ---")
for livro in livros:
    if livro['ano'] >= 2020:
        print(livro)