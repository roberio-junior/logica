#   Escreva um programa que implemente duas “matrizes” 2x2, ou seja, uma
# lista contendo duas listas de tamanho 2. O programa deve receber valores
# para as duas listas 2x2 e criar uma terceira matriz que é a matriz soma
# das anteriores e imprimi-la ao final.

matriz1 = []
matriz2 = []
matriz_soma = []

print("Digite os valores da primeira matriz 2x2:")
for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Elemento [{i+1}][{j+1}]: "))
        linha.append(valor)
    matriz1.append(linha)

print("\nDigite os valores da segunda matriz 2x2:")
for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Elemento [{i+1}][{j+1}]: "))
        linha.append(valor)
    matriz2.append(linha)

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(matriz1[i][j] + matriz2[i][j])
    matriz_soma.append(linha)

print("\nMatriz soma:")
for linha in matriz_soma:
    print(linha)
