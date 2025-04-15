#   Construa um programa que lê um conjunto de 30 valores e os coloca em 2
# listas conforme estes valores forem pares ou ímpares. O tamanho da lista
# deve ser de 5 posições. Se alguma lista estiver “cheia”, o programa deve
# exibir seus elementos. Ao terminar a leitura dos 30 elementos também deve
# escrever o conteúdo das duas listas. Cada lista pode ser preenchida
# quantas vezes for necessário.

pares = []
impares = []

for i in range(30):

    num = int(input(f"Digite o {i + 1}º número: "))

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    if len(pares) == 5:
        print("Lista de pares cheia:", pares)
        pares = []
        print("A lista de números pares foi limpa!")

    if len(impares) == 5:
        print("Lista de impares cheia:", impares)
        impares = []
        print("A lista de números impares foi limpa!")

if pares:
    print("Elementos restantes na lista de pares:", pares)

if impares:
    print("Elementos restantes na lista de ímpares:", impares)
