#   Escreva um programa que leia as notas dos alunos de uma disciplina (A
# quantidade de alunos deve ser informada pelo usuário) e informe quantos
# alunos estão abaixo da média e quantos estão na média. (Considere a nota
# sendo um inteiro de 0 a 100 e a média 60).

acima = []
abaixo = []

quantidade = (int(input("Informe a quantidade de alunos matriculados: ")))

for i in range(quantidade):

    nota = int(input(f"Digite uma nota de 0 a 100 para o {i+1}º aluno: "))
    
    if nota >= 60:
        acima.append(nota)
    else:
        abaixo.append(nota)

alunosabaixo = len(abaixo)
alunosacima = len(acima)

print(f"Alunos abaixo da média: {alunosabaixo}\nAlunos na média: {alunosacima}")
