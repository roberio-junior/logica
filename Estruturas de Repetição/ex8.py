#   Desenvolva um programa em Python que determine o pagamento bruto de
# cada um de vários empregados. A companhia paga o valor de uma "hora
# normal" pelas primeiras 40 horas trabalhadas de cada empregado e paga
# o valor de uma "hora extra" (uma vez e meia a hora normal) para cada
# hora trabalhada depois de completadas as primeiras 40 horas. Você
# recebeu uma lista de empregados da companhia, o número de horas que
# cada empregado trabalhou durante a semana passada e o valor da "hora
# normal" de cada empregado. Seu programa deve receber essas informações
# de cada empregado além de determinar e exibir o pagamento bruto do empregado.

salario=0
horas=0

while horas != -1:
    horas=int(input('Entre com o número de horas trabalhadas(-1 para finalizar):'))

    if horas!=-1:
        valor=float(input('Entre com o valor da hora normal do trabalhador C$00.00):'))
        if horas<=40:
            salario=horas*valor
        elif horas>40:
            horas=horas-40
            valor=valor*1.5
            salario=400+(horas*valor)

        print("Salário= %.2f" %salario)