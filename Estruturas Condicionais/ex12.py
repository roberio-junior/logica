a = float(input("Digite o valor do lado A do triângulo: "))
b = float(input("Digite o valor do lado B do triângulo: "))
c = float(input("Digite o valor do lado C do triângulo: "))

if abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
    if a == b == c:
        tipo = "Equilátero"
    elif a == b or a == c or b == c:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    print(f"Os valores informados formam um triângulo {tipo}.")
else:
    print("Os valores informados NÃO formam um triângulo.")
