#   Construa um programa que leia a categoria de um produto e
# determine o preço, conforme a tabela abaixo:

#   Categoria | Preço
#   1         | 10,00
#   2         | 18,00
#   3         | 23,00
#   4         |26,00
#   5         | 31,00

categoria = int(input("Digite a categoria do produto (1 a 5): "))
    
if categoria == 1:
    preco = 10.00
elif categoria == 2:
    preco = 18.00
elif categoria == 3:
    preco = 23.00
elif categoria == 4:
    preco = 26.00
elif categoria == 5:
    preco = 31.00
else:
    preco = "Categoria inválida"
    
print("O preço do produto é: R$%.2f" %preco)