#   A confederação brasileira de natação irá promover eliminatórias
# para o próximo mundial. Fazer um algoritmo em Python que receba a
# idade de um nadador e determine (imprima) a sua categoria segundo a
# tabela a seguir:

#   Categoria  | Idade
#   Infantil A | 5 – 7 anos
#   Infantil B | 8 – 10 anos
#   Juvenil A  | 11 – 13 anos
#   Juvenil B  | 14 – 17 anos
#   Sênior     | Maiores de 18 anos

idade = int(input("Digite a idade do nadador: "))

if idade >= 5 and idade <= 7:
    categoria = "Infantil A"
elif idade >= 8 and idade <= 10:
    categoria = "Infantil B"
elif idade >= 11 and idade <= 13:
    categoria = "Juvenil A"
elif idade >= 14 and idade <= 17:
    categoria = "Juvenil B"
elif idade >= 18:
    categoria = "Sênior"
else:
    categoria = "Idade fora das categorias disponíveis"

print(f"O nadador tem {idade} anos e pertence à categoria: {categoria}.")
