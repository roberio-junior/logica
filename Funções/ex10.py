#   Crie uma função em linguagem PYTHON que retorna a enésima potência de
# uma variável real x.

def potencia(x, n):
    return x ** n 

base = float(input("Digite o valor da base (x): "))
expoente = int(input("Digite o valor do expoente (n): "))

print(f"O resultado de {base}^{expoente} é: {potencia(base, expoente)}")
