#   Construa um programa bancário para aprovação de empréstimos. O
# programa deve receber o valor do empréstimo solicitado, o salário do
# cliente e a quantidade de meses para se pagar o empréstimo. O valor
# da prestação mensal não pode ultrapassar 30% do salário. O programa
# deve considerar o valor da prestação como sendo o valor solicitado
# dividido pela quantidade de meses.

valor_emprestimo = float(input("Digite o valor do empréstimo solicitado: R$"))

salario = float(input("Digite o salário do cliente: R$"))

meses = int(input("Digite a quantidade de meses para pagar o empréstimo:"))

prestacao_mensal = valor_emprestimo / meses

limite_prestacao = salario * 0.30

if prestacao_mensal <= limite_prestacao:
    print("\nEmpréstimo aprovado! O valor da prestação mensal será de R$%.2f" %prestacao_mensal)
else:
    print("\nEmpréstimo não aprovado! O valor da prestação mensal de R$%.2f ultrapassa 30%% do seu salário, que é R$%.2f." %(prestacao_mensal, limite_prestacao))
