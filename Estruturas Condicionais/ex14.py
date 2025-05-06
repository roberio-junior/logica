frequencia = float(input("Digite a frequência do aluno (0 a 100%): "))
nota = float(input("Digite a nota do aluno (0.0 a 10.0): "))

if frequencia < 75:
    situacao = "Reprovado"
elif nota < 3.0:
    situacao = "Reprovado"
elif 3.0 <= nota < 7.0:
    situacao = "4ª Prova"
else:
    situacao = "Aprovado"

print(f"Frequência: {frequencia:.1f}%\nNota: {nota:.1f}\nSituação: {situacao}")
