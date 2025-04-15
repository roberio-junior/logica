#   Construa um programa que leia duas listas de 10 posições e faça a
# multiplicação dos elementos de mesmo índice, colocando o resultado em uma
# terceira lista. Mostre a lista resultante.

lista1 = []
lista2 = []
resultante = []


for i in range(10):

    num = int(input(f"Digite o {i + 1}º número da lista 1: "))

    lista1.append(num)

print("Lista 1 completa!")
print("-" * 40)

for i in range(10):

    num = int(input(f"Digite o {i + 1}º número da lista 2: "))

    lista2.append(num)

print("Lista 2 completa!")
print("-" * 40)

for i in range(10):
    num = lista1[i] * lista2[i]
    resultante.append(num)

print("Lista resultante:", resultante)