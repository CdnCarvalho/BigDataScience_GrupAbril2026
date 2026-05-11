# Lista para armazenar as notas dos 5 estudantes
medias = []
QUANTIDADE_ESTUDANTES = 5
# Coletando as notas dos estudantes
for i in range(QUANTIDADE_ESTUDANTES):
    nota1 = float(input(f"\nDigite a nota1 do {i+1}º estudante: "))
    nota2 = float(input(f"Digite a nota2 do {i+1}º estudante: "))
    nota3 = float(input(f"Digite a nota3 do {i+1}º estudante: "))
    nota4 = float(input(f"Digite a nota4 do {i+1}º estudante: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4    
    medias.append(media)
    
for i, m in enumerate(medias):
    print(i, m)
    print(f"\nEstudante {i+1}:")
    if m >= 7:
        print(f"Aprovado, média: {m:.2f}")
    else:
        print(f"Reprovado, média: {m:.2f}")
# -------------------------------------------------------------------------------


# versão 2
medias = []
QUANTIDADE_ESTUDANTES = 3
# Coletando as notas dos estudantes
for i in range(QUANTIDADE_ESTUDANTES):    
    print(f'\nEstudante {i+1}')
    notas = []
    for n in range(4):
        nota = float(input(f"Digite a nota do {n+1}º estudante: "))
        notas.append(nota)
    
    media = sum(notas) / 4
    medias.append(media)

# motrando as avaliações de todos
for i, media in enumerate(medias):
    print(i, media)
    print(f"\n{i+1}º estudante\nMédia: {media}")
    if media >= 7:
        print(f"\n{i+1}º estudante\nAprovado\nMédia: {media}")
    else:
        print(f"\n{i+1}º estudante\nReprovado\nMédia: {media}")
# ------------------------------------------------------------------------------------