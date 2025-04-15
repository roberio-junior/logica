#    Escreva um programa em Python que utilize um loop para produzir a
# seguinte tabela de valores:

# A  | A+2 | A+4 | A+6
# 3  | 5   | 7   | 9
# 6  | 8   | 10  | 12
# 9  | 11  | 13  | 15
# 12 | 14  | 16  | 18
# 15 | 17  | 19  | 21

print('A \tA+2 \tA+4 \tA+6')
for a in range(3,16,3):
    a2=a+2
    a4=a+4
    a6=a+6
    print(f'{a}\t{a2}\t{a4}\t{a6}')