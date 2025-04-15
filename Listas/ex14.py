#   Escreva um programa que leia uma lista S de tamanho 20 e uma variável A.
# A seguir, mostre o produto da variável A pela lista.

S = []
for i in range(20):
    num = float(input(f"Digite o {i+1}º número da lista S: "))
    S.append(num)

A = float(input("Digite o valor da variável A: "))

produto = [] 
for i in S:
    produto.append(A * i) 

print("Produto da variável A pela lista S:", produto)