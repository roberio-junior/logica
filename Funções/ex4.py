#   Crie uma função em linguagem Python que receba 2 números e retorne
# o maior valor.

def maiorNumero(num1, num2):
    if num1 > num2:
        resultado = f"O maior numero é o {num1}."
    elif num2 > num1:
        resultado = f"O maior numero é o {num2}."
    else:
        resultado = "Os números são iguais."

    return resultado

numero1 = float(input("Informe o 1º número: "))
numero2 = float(input("Informe o 2º número: "))

resultado = maiorNumero(numero1, numero2)

print(resultado)