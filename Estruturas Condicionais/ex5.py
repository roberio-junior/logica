#   A CEF concederá um crédito especial com juros de 2% aos seus
# clientes de acordo com o saldo médio no último ano. Fazer um
# algoritmo em Python que leia o saldo médio de um cliente e calcule o
# valor do crédito de acordo com a tabela a seguir. Imprimir uma
# mensagem informando o saldo médio e o valor de crédito.

#   Saldo Médio    | Percentual
#   De 0 a 500     | Nenhum crédito
#   De 501 a 1000  | 30% do valor do saldo médio
#   De 1001 a 3000 | 40% do valor do saldo médio
#   Acima de 3000  | 50% do valor do saldo médio

saldo_medio = float(input("Digite o saldo médio do último ano: "))

if saldo_medio >= 0 and saldo_medio <= 500:
    credito = 0
elif saldo_medio <= 1000:
    credito = saldo_medio * 0.3
elif saldo_medio <= 3000:
    credito = saldo_medio * 0.4
else:
    credito = saldo_medio * 0.5

print(f"Saldo Médio: R$ {saldo_medio:.2f}")
print(f"Crédito Concedido: R$ {credito:.2f}")
