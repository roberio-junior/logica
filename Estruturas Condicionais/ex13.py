#   Criar um algoritmo em Python que receba o valor de x, e calcule e
# imprima o valor de f(x).

#   f(x)          | Condição 
#   1             | x <=1
#   2             | 1 < x <=3
#   x ao quadrado | 2 <x <=3
#   x ao cubo     | x  >3

x = float(input("Digite o valor de x: "))

if x <= 1:
    f_x = 1
elif 1 < x <= 2:
    f_x = 2
elif 2 < x <= 3:
    f_x = x ** 2
else:
    f_x = x ** 3

print(f"O valor de f({x}) é: {f_x:.2f}")
