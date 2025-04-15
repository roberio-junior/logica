#   Escreva um programa que leia uma lista K de tamanho 30. Troque, a
# seguir, todos os elementos de ordem ímpar da lista com os elementos de
# ordem par imediatamente posteriores.

k = []

for i in range(30):

    num = int(input(f"Digite o {i + 1}º número: "))

    k.append(num)

for i in range(0, 30, 2):
    k[i], k[i + 1] = k[i + 1], k[i]

print(k)