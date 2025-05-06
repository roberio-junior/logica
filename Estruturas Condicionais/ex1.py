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