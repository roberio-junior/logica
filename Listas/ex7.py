#   Construa um programa que lê n números armazenando-os em uma lista de
# inteiros. Após isso o programa processa e retorna a quantidade de
# elementos da lista que são números negativos.

n = int(input("Informe quantos números serão armazenados na lista: "))

numeros = []

for i in range(n):

    num = int(input(f"Digite o {i + 1}º número: "))

    numeros.append(num)

negativos = 0

for i in range (n):
    
    if numeros[i] < 0:
        negativos += 1

print(f"Quantidade de elementos da lista que são números negativos: {negativos}")