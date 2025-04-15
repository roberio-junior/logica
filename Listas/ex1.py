# 1. Escreva um programa que leia 10 inteiros e armazene-os em uma lista a,
# e em seguida mostre todos os dados da lista.

a = []

i = 0
while i < 10:
    num = int(input("Informe um número inteiro: "))
    a.append(num)
    i += 1

print("lista: ", a)