#   Encontre os dois maiores valores de 10 números.
# Nota: Cada número só pode ser fornecido uma única vez.

maior1 = int(input("Digite o 1º número: "))
maior2 = int(input("Digite o 2º número: "))

if maior2 > maior1:
    maior1, maior2 = maior2, maior1

for i in range(8):
    num = int(input(f"Digite o {i + 3}º número: "))

    if num > maior1:
        maior2 = maior1
        maior1 = num
    elif num > maior2 and num != maior1:
        maior2 = num

print(f"Os dois maiores números são: {maior1} e {maior2}")