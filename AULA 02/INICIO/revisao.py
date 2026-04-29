print('Hello Word')

qtd_vendida = 20
valor = 15
total = qtd_vendida * valor
print(total)

# Desconto de 12% sobre o total
desconto = total * 0.12
total = total - desconto
print(total)

# Uso dos parênteses
# Pagar dois produtos em 2x parcelas. Produto1 parcela de R$ 40, Produto2 parcela de R$ 30
parcela1 = 40
parcela2 = 30
resultado = (40 + 30) * 2
print(resultado)



# EXEMPLO 3 - Algoritmos com mais de uma operação
# Enunciado: Calcule o valor total de uma compra com desconto de 10%.
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))
total = preco * quantidade
desconto = total * 0.1
valor_final = total - desconto
print("O valor total da compra com desconto é:", valor_final)