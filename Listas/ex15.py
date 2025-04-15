#   Faça um programa que lê as notas de n (o usuário deve informar)
# alunos, cada nota é um inteiro entre 0 e 100, e imprima a quantidade de
# vezes com que apareceu cada nota.

n = int(input("Informe a quantidade de alunos: "))

notas = []

i = 0
while i < n:

    nota = int(input(f"Digite a nota do {i+1}º aluno (0 a 100): "))

    if 0 <= nota <= 100:
        notas.append(nota)
        i += 1
    else:
        print("Nota inválida! Digite um valor entre 0 e 100.")

notas_contadas = []

print("Frequência das notas:")

for nota in notas:
    if nota not in notas_contadas:
        qtd = 0
        for x in notas:
            if x == nota:
                qtd += 1
        notas_contadas.append(nota)
        if qtd > 1:
            print(f"Nota {nota}: {qtd} vezes")
        else:
            print(f"Nota {nota}: {qtd} vez")
