#   Construa um programa que lê uma lista de 10 números lidos do teclado e
# os apresenta na tela em ordem inversa a lida.

numeros = []
for i in range(10):

    num = int(input(f"Digite o {i + 1}º número: "))

    numeros.append(num)

for i in range(9, -1, -1):

    print(numeros[0])