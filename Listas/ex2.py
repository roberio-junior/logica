#   Escreva um programa que leia 10 inteiros e armazene-os em uma lista a.
# O programa deve informar qual o maior e o menor número digitado.

a = []

maior = int(input("Digite o 1º número: "))
menor = int(input("Digite o 2º número: "))
a.append(maior)
a.append(menor)

if menor > maior:
    maior, menor = menor, maior

for i in range(8):

    num = int(input(f"Digite o {i + 3}º número: "))

    if num > maior:
        maior = num

    if num > menor:
        menor = num
    
    a.append(num)

print(f'Maior número: {maior}, Menor número: {menor}')