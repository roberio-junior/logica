# 1. Defina a função exibeMenu() para exibir as opções:
# • Sair
# • Somar
# • Subtrair
# • Multiplicar
# • Dividir
# 2. Implemente as seguintes funções:
# • Somar(numero1, numero2)
# • Subtrair(numero1, numero2)
# • Multiplicar(numero1, numero2)
# • Dividir(numero1, numero2)
# 3. Altere o programa principal para executar os métodos acima conforme escolha do usuário.

def exibeMenu():
    print("##### MENU #####\n")
    print("0- SAIR\n")
    print("1 - SOMAR\n")
    print("2 - SUBTRAIR\n")
    print("3 - MULTIPLICAR\n")
    print("4 - DIVIDIR\n")
    opcao = int(input("Escolha uma opção: "))
    return opcao

def somar(numero1, numero2):
    resultado = numero1 + numero2
    return f"Resultado: {resultado}"

def subtrair(numero1, numero2):
    resultado = numero1 - numero2
    return f"Resultado: {resultado}"

def multiplicar(numero1, numero2):
    resultado = numero1 * numero2
    return f"Resultado: {resultado}"

def dividir(numero1, numero2):
    if numero2 == 0:
        return "Erro! Divisão por zero."
    else:
        resultado = numero1 / numero2
        return f"Resultado: {resultado}"

i = 0
opcao = 1
num1 = 0
num2 = 0
resultado = 0

while opcao != 0:
    opcao = exibeMenu()
    if opcao == 0:
        print("Encerrando o programa...")
        break

    elif opcao in [1, 2, 3, 4]:
        num1 = float(input("Informe o primeiro número para a operação: "))
        num2 = float(input("Informe o segundo número para a operação: "))

    else:
        print("Opção Inválida!")

    if opcao == 1:
        resultado = somar(num1, num2)

    elif opcao == 2:
        resultado = subtrair(num1, num2)

    elif opcao == 3:
        resultado = multiplicar(num1, num2)

    elif opcao == 4:
        resultado = dividir(num1, num2)

    print(resultado)