# Construa um algoritmo em Python para determinar a situação
# (APROVADO / QUARTA PROVA / REPROVADO) de um aluno, dado a sua
# freqüência (porcentagem de 0 a 100%) e sua nota (nota de 0.0 a 10.0),
# sendo que:

#Condição                                            | Situação
#Freqüência até 75%                                  | Reprovado
#Freqüência entre 75% e 100% e Nota até 3.0          | Reprovado
#Freqüência entre 75% e 100% e Nota de 3.0 até 7.0   | 4ª Prova
#Freqüência entre 75% e 100% e Nota entre 7.0 e 10.0 | Aprovado

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
