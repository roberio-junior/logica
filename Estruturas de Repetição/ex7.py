#   Uma grande companhia química paga seus vendedores por comissão. Os
# vendedores recebem $200 por semana mais 9 por cento de suas vendas
# brutas naquela semana. Por exemplo, um vendedor que vender o
# equivalente a $5000 em produtos químicos em uma semana recebe $200
# mais 9 por cento de $5000, ou um total de $650. Desenvolva um
# programa em Python que receba as vendas brutas de cada vendedor na
# última semana, calcule seu salário e o exiba. Processe os dados de um
# vendedor de cada vez.

i=0
while i != -1:
    i=float(input("Entre com a venda em dólares(-1 para finalizar):"))
    if i != -1:
        salario=200+(i*0.09)
        print(f'Salário: {salario:.2f}')