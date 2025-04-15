#   Escreva um algoritmo em Python que dada a idade de uma pessoa,
# determine sua classificação segundo a seguinte tabela:

#   -maior de idade;
#   -menor de idade;
#   -pessoa idosa (idade superior ou igual a 65 anos).

idade = int(input("Digite a idade da pessoa: "))

if idade >= 18:
    classificacao = "Maior de idade"
    if idade >= 65:
        classificacao = "Pessoa idosa"
else:
    classificacao = "Menor de idade"

print(f"A pessoa tem {idade} anos e é classificada como: {classificacao}.")
