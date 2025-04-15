#   Crie uma função em linguagem PYTHON que receba um valor em metros e
# retorne o correspondente em centímetros.

def metros_para_centimetros(metros):
    return metros * 100

valor_metros = float(input("Digite o valor em metros: "))
print(f"O valor em centímetros é: {metros_para_centimetros(valor_metros)} cm")
