#   Crie um algoritmo em Python que leia a idade de uma pessoa e
# informe a sua classe eleitoral:

#   -não eleitor (abaixo de 16 anos);
#   -eleitor obrigatório (entre a faixa de 18 e menor de 65 anos);
#   -eleitor facultativo (de 16 até 18 anos e maior de 65 anos, inclusive).

idade = int(input("Digite a idade da pessoa: "))

if idade < 16:
    classe = "Não eleitor"
elif 18 <= idade < 65:
    classe = "Eleitor obrigatório"
else:
    classe = "Eleitor facultativo"

print(f"A pessoa tem {idade} anos e pertence à classe eleitoral: {classe}.")
