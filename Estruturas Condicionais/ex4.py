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
