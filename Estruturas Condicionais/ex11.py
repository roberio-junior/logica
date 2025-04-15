#   Dado três valores, A, B e C, construa um algoritmo em Python para
# verificar se estes valores podem ser valores dos lados de um triângulo. 

#   "Só irá existir um triângulo se, somente se, os seus lados
# obedeceram à seguinte regra: um de seus lados deve ser maior que o
# valor absoluto (módulo)* da diferença dos outros dois lados e menor
# que a soma dos outros dois lados."

#   | b - c | < a < b + c |
#   | a - c | < b < a + c |
#   | a - b | < c < a + b |

#   Dica: Utilize a função abs() para encontrar um módulo de um número.

a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

if abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
    print("Os valores informados podem formar um triângulo.")
else:
    print("Os valores informados NÃO formam um triângulo.")
