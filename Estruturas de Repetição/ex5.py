#   Desenvolva um programa que imprima o 25º número da sequência de Fibonacci na tela.

contador = 1
n1 = 0
n2 = 1
while contador <= 25:
    aux = n1
    n1 = n2
    n2 += aux
    contador += 1

print(aux)