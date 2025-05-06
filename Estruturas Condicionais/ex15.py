frequencia = float(input("Digite a frequência do aluno (0 a 100%): "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if frequencia < 75:
    situacao = "Reprovado"
elif media < 3.0:
    situacao = "Reprovado"
elif 3.0 <= media < 7.0:
    if nota1 < 3.0 or nota2 < 3.0:
        situacao = "Reprovado"
    else:
        situacao = "4ª Prova"
else:
    situacao = "Aprovado"

print(f"Frequência: {frequencia:.1f}%\nMédia: {media:.2f}\nSituação: {situacao}")
