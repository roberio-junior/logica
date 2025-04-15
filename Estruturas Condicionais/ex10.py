#   Escreva um algoritmo em Python que leia as notas das unidades de um
# aluno e determine a média das notas semestral. Através da média
# calculada o algoritmo deve imprimir a seguinte mensagem: “Aprovado”,
# “Reprovado” ou em “Quarta Prova” (a média é 7 para "Aprovação", menor
# que 3 para "Reprovação" e as demais em "Quarta Prova").

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
