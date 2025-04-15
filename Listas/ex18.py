#   Escreva um algoritmo que leia uma lista de 15 posições e mostre-a
# ordenada de modo crescente.

numeros = []

for i in range(15):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

for i in range(len(numeros) - 1):
    for j in range(len(numeros) - 1 - i):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("\nLista ordenada em ordem crescente:", numeros)

