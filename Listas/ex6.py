#   construa um programa que lê uma lista de 10 números inteiros positivos,
# lidos do teclado e substitua cada elemento ímpar por -1 e os pares por 1.

numeros = []
for i in range(10):

    num = int(input(f"Digite o {i + 1}º número: "))

    numeros.append(num)

for i in range (10):
    
    if numeros[i] % 2 == 0:
        numeros[i]  = 1
    else:
        numeros[i] = -1

print(numeros)