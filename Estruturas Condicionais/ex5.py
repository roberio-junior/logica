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
