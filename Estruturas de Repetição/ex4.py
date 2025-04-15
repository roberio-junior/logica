#   Desenvolva um programa que imprima os 100 primeiros números da
# sequência de Fibonacci na tela. [0,1,1,2,3,5,8,13,21,34...]

contador = 1
n1 = 0
n2 = 1
while contador <= 100:
    aux = n1
    n1 = n2
    n2 += aux
    contador += 1
    print(aux)
