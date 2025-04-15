#   Desenvolva um programa que leia a altura (em metros) e o peso (em
# quilogramas) e calcule o IMC - Índice de Massa Corporal do usuário e
# informe sua situação corporal conforme tabela abaixo. O cálculo do
# IMC é feito dividindo-se o peso pela altura ao quadrado. Sabe-se
# ainda que a tabela abaixo é válida apenas para pessoas acima dos 15
# anos de idade, então o programa deverá invalidar os cálculos que
# fujam dessa regra.

#   RESULTADO          | SITUAÇÃO
#   Abaixo de 17       | Muito abaixo do peso
#   Entre 17 e 18,49   | Abaixo do peso
#   Entre 18,5 e 24,99 | Peso normal
#   Entre 25 e 29,99   | Acima do peso
#   Entre 30 e 34,99   | Obesidade I
#   Entre 35 e 39,99   | Obesidade II (severa)
#   Acima de 40        | Obesidade III (mórbida)

idade = int(input("Digite a sua idade: "))
altura = float(input("Digite a sua altura (em metros): "))
peso = float(input("Digite o seu peso (em quilogramas): "))

if idade <= 15:
    print("Cálculo do IMC não permitido para pessoas com 15 anos ou menos.")

else:
    imc = peso / (altura ** 2)
    print("\nSeu IMC é: %.2f" %imc)

    if imc < 17:
        situacao = "Muito abaixo do peso"

    elif imc >= 17 and imc <= 18.49:
        situacao = "Abaixo do peso"

    elif imc > 18.49 and imc <= 24.99:
        situacao = "Peso normal"

    elif imc > 24.99 and imc <= 29.99:
        situacao = "Acima do peso"

    elif imc > 29.99 and imc <= 34.99:
        situacao = "Obesidade I"

    elif imc > 34.99 and imc <= 39.99:
        situacao = "Obesidade II (severa)"

    else:
        situacao = "Obesidade III (mórbida)"

    print("Sua situação corporal é:", situacao)
