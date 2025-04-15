#   Escreva um algoritmo em Python que leia as notas das unidades de um
# aluno e sua frequência (porcentagem de 0 a 100%). Através da média
# calculada e da frequência, o algoritmo deve determinar a situação
# (APROVADO / QUARTA PROVA / REPROVADO).

#   Condição                                                                          | Situação
#   Freqüência até 75%                                                                | Reprovado
#   Freqüência entre 75% e 100% e média até 3.0                                       | Reprovado
#   Freqüência entre 75% e 100% e média de 3.0 até 7.0 e notas inferiores a 3.0.      | Reprovado
#   Freqüência entre 75% e 100% e média de 3.0 até 7.0 e notas acima ou iguais a 3.0. | 4ª Prova
#   Freqüência entre 75% e 100% e média entre 7.0 e 10.0                              | Aprovado

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
