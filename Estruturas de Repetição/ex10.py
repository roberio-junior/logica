#   Escreva um programa em Python que utilize um loop para imprimir a
# seguinte tabela de valores:

# N  | 10*N | 100*N | 1000* N
# 1  | 10   | 100   | 1000
# 2  | 20   | 200   | 2000
# 3  | 30   | 300   | 3000
# 4  | 40   | 400   | 4000
# 5  | 50   | 500   | 5000
# 6  | 60   | 600   | 6000
# 7  | 70   | 700   | 7000
# 8  | 80   | 800   | 8000
# 9  | 90   | 900   | 9000 
# 10 | 100  | 1000  | 10000

print('N\t10*N\t100*N\t1000*N')
n=1
while n<=10:
    n10=n*10
    n100=n*100
    n1000=n*1000
    print(f"{n}\t{n10}\t{n100}\t{n1000}")
    n+=1