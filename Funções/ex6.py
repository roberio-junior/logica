#   Crie uma função em linguagem PYTHON que receba 3 números e retorne
# o maior valor.

def maiorNumero():
    iguais = True

    for i in range(1,4):
        num = float(input(f"Informe o {i}º número: "))

        if i == 1:
            aux = num
            maior  = num
        elif num > maior:
            maior = num

        if aux != num:
            iguais = False
        aux = num

    if iguais:
        resultado = "Os números são iguais."
    else:
        resultado = f"O maior numero é o {maior}."
    
    return resultado

resultado = maiorNumero()
print(resultado)
