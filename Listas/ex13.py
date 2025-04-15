#   Escreva um programa que leia uma lista de 20 posições e mostre-a. Em
# seguida, troque o primeiro elemento com o último, o segundo com o
# penúltimo, o terceiro com o antepenúltimo, e assim sucessivamente.
# Mostre a nova lista depois das trocas.

numeros = []

for i in range(20):

    num = int(input(f"Digite o {i + 1}º número: "))

    numeros.append(num)

for i in range(10):
    numeros[i], numeros[19 - i] = numeros[19 - i], numeros[i]

print("Nova lista:", numeros)