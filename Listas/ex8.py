#   Construa um programa que lê n números armazenando-os em uma lista de
# inteiros "a" e lê um valor inteiro "x" e retorna a quantidade de vezes
# que "x" aparece na lista "a".

n = int(input("Informe quantos números serão armazenados na lista: "))
a = []
quantidade = 0

for i in range(n):

    num = int(input(f"Digite o {i + 1}º número: "))

    a.append(num)

x = int(input("Digite o número que deseja contar na lista: "))

for i in range(n):
    if a[i] == x:
        quantidade += 1

print(f"O número {x} aparece {quantidade} na lista")