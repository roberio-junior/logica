#   Depois da liberação do governo para as mensalidades dos planos de
# saúde, as pessoas começaram a fazer pesquisas para descobrir um bom
# plano, não muito caro. Um vendedor de um plano de saúde apresentou a
# tabela a seguir. Criar um algoritmo em Python que entre com a idade
# de uma pessoa e imprima o valor que ela deverá pagar, segundo a
# seguinte tabela:

#   Idade                   | Valor
#   Até 10 anos             | R$ 30,00
#   Acima de 10 até 29 anos | R$ 60,00
#   Acima de 29 até 45 anos | R$ 120,00
#   Acima de 45 até 59 anos | R$ 150,00
#   Acima de 59 até 65 anos | R$ 250,00
#   maior que 65 anos       | R$ 400,00

idade = int(input("Digite a idade da pessoa: "))

if idade <= 10:
    valor = 30.00
elif idade <= 29:
    valor = 60.00
elif idade <= 45:
    valor = 120.00
elif idade <= 59:
    valor = 150.00
elif idade <= 65:
    valor = 250.00
else:
    valor = 400.00

print(f"A pessoa tem {idade} anos e o valor do plano de saúde é: R$ {valor:.2f}")
