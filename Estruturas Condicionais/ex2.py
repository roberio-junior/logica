#   Construa um programa que leia dois números e pergunte ao usuário qual
# operação ele deseja executar: soma, subtração, multiplicação ou
# divisão. Após a operação o programa deve exibir o resultado do
# processamento.

print("=" * 30)
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("=" * 30)

opcao = input("Digite o número da operação desejada (1/2/3/4): ")

num1 = float(input("Digite o primeiro número da operação: "))
num2 = float(input("Digite o segundo número da operação: "))

if opcao == '1':
    resultado = num1 + num2
    print("Resultado da soma: %.2f" %resultado)

elif opcao == '2':
    resultado = num1 - num2
    print("Resultado da subtração: %.2f" %resultado)

elif opcao == '3':
    resultado = num1 * num2
    print("Resultado da multiplicação: %.2f" %resultado)

elif opcao == '4':
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado da divisão: %.2f" %resultado)
    else:
        print("Erro! Divisão por zero.")

else:
    print("Operação inválida.")