idade = int(input("Digite a idade da pessoa: "))

if idade < 16:
    classe = "Não eleitor"
elif 18 <= idade < 65:
    classe = "Eleitor obrigatório"
else:
    classe = "Eleitor facultativo"

print(f"A pessoa tem {idade} anos e pertence à classe eleitoral: {classe}.")
