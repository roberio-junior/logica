#   Escreva um programa que receba uma lista com 5 números inteiros. Em
# seguida, determine e imprima na tela o maior elemento par da lista (se
# houver), o menor elemento ímpar da lista (se houver), o somatório dos
# elementos da lista e a média.

numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

maior_par = None
menor_impar = None
soma = 0

for num in numeros:
    soma += num 

    if num % 2 == 0:
        if maior_par is None or num > maior_par:
            maior_par = num

    if num % 2 != 0:
        if menor_impar is None or num < menor_impar:
            menor_impar = num

media = soma / 5

if maior_par is not None:
    print(f"Maior número par: {maior_par}")
else:
    print("Nenhum número par encontrado.")

if menor_impar is not None:
    print(f"Menor número ímpar: {menor_impar}")
else:
    print("Nenhum número ímpar encontrado.")

print(f"Soma dos elementos: {soma}")
print(f"Média dos elementos: {media:.2f}")
