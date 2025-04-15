#   Modifique o programa escrito no Exercício 13 de forma que seja
# impresso um quadrado vazado. Por exemplo, se seu programa lesse um
# tamanho 5, deveria imprimir:

# *****
# *   *
# *   *
# *   *
# *****

asteriscos=int(input('Informe quantos asteriscos cada lado do quadrado tem: '))
contador = 1 
while contador <= asteriscos:
    if contador == 1 or contador == asteriscos:
        print('*' * asteriscos)
    else:
        print('*' + ' ' * (asteriscos-2) + '*')
    contador+=1