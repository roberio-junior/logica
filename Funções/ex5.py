# Crie uma função em linguagem PYTHON que receba 2 números e retorne
# o menor valor.

def menorNumero(num1, num2):
    if num1 < num2:
        resultado = f"O menor numero é o {num1}."
    elif num2 < num1:
        resultado = f"O menor numero é o {num2}."
    else:
        resultado = "Os números são iguais."

    return resultado

numero1 = float(input("Informe o 1º número: "))
numero2 = float(input("Informe o 2º número: "))

resultado = menorNumero(numero1, numero2)

print(resultado)