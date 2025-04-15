# Crie uma função em linguagem PYTHON que receba 3 números e retorne
# o menor valor.

def menorNumero():
    iguais = True

    for i in range(1, 4):
        num = float(input(f"Informe o {i}º número: "))

        if i == 1:
            aux = num
            menor = num
        elif num < menor:
            menor = num

        if aux != num:
            iguais = False
        aux = num

    if iguais:
        resultado = "Os números são iguais."
    else:
        resultado = f"O menor número é {menor}."
    
    return resultado

resultado = menorNumero()
print(resultado)
