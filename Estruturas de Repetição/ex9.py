#   O processo de encontrar o maior número (i.e., o máximo de um
# conjunto de números) é usado freqüentemente em aplicações
# computacionais. Por exemplo, um programa que determinasse o vencedor
# de um concurso de vendas receberia o número de unidades vendidas por
# vendedor. O vendedor que tivesse vendido mais unidades venceria o
# concurso. Escreva um programa em Python que receba uma série de 10
# números, determine o maior deles e o imprima. Sugestão: Seu programa
# deve usar três variáveis da seguinte maneira:

# ● contador: Um contador para contar até 10 (i.e., para controlar
# quantos números foram fornecidos e para determinar quando todos os 10
# números foram processados),

# ● num: O número atual fornecido ao programa,
# ● maior: O maior número encontrado em cada instante.

contador=0
while contador<10:
    num=int(input('Digite um número da série:'))
    if contador==0:
            maior=num
    elif num>maior:
        maior=num
    contador+=1
print(f"O maior número digitado foi: {maior}")