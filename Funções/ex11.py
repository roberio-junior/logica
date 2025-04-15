#   Crie uma função em linguagem PYTHON que receba um valor e retorne o
# seu fatorial.

def fatorial(n):
    if n < 0:
        return "Fatorial não definido para números negativos."
    elif n == 0 or n == 1:
        return f"O fatorial de {n} é: 1"
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return f"O fatorial de {n} é: {resultado}"

numero = int(input("Digite um número inteiro para calcular o fatorial: "))
print(fatorial(numero))
