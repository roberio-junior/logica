#   Escreva um programa que leia o lado de um quadrado e então imprima
# o quadrado com asteriscos. Seu programa deve funcionar com quadrados
# de todos os tamanhos entre 1 e 20. Por exemplo, se seu programa lesse
# um tamanho 4, deveria imprimir:

# ****
# ****
# ****
# ****

asteriscos=int(input('Informe quantos asteriscos cada lado do quadrado tem: '))
contador=0
while contador<asteriscos:
    print('*'*asteriscos)
    contador+=1