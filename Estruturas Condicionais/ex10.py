nota1 = float(input("Digite a primeira nota (0 a 10): "))
nota2 = float(input("Digite a segunda nota: (0 a 10)"))
media = (nota1 + nota2) / 2

if media >= 7:
    situacao = "Aprovado"
elif media < 3:
    situacao = "Reprovado"
else:
    situacao = "Quarta Prova"

print(f"Média: {media:.2f}\nSituação: {situacao}")
