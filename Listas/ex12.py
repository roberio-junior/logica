#   . Escreva um programa que leia e mostre uma lista de 20 números. A
# seguir, conte quantos valores pares existem na lista.

numeros = []

for i in range(5):

    num = int(input(f"Digite o {i + 1}º número: "))

    numeros.append(num)

pares = 0

for i in range (5):
    
    if numeros[i] % 2 == 0:
        pares += 1

print(f"Existem {pares} valores pares na lista.")