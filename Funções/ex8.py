#   Construa um programa com uma função exibeOpcoes que imprime as opções
# de executar as funções das questões anteriores e lê a opção escolhida
# pelo usuário, essa função deve retornar o valor lido. O programa deve
# implementar a função main de forma a invocar a função exibeOpcoes e
# invocando as funções das questões anteriores de acordo com a escolha do
# usuário. Para sair o usuário deve digitar a opção zero.

def exibeOpcoes():
    print("\nEscolha uma opção:")
    print("1 - Encontrar o maior número")
    print("2 - Encontrar o menor número")
    print("0 - Sair")
    
    opcao = int(input("Digite a opção desejada: "))
    return opcao

def maiorNumero():
    iguais = True
    qtd = int(input("Quantos números você deseja fornecer? "))

    for i in range(1, qtd + 1):
        num = float(input(f"Informe o {i}º número: "))

        if i == 1:
            aux = num
            maior = num
        elif num > maior:
            maior = num

        if aux != num:
            iguais = False
        aux = num

    if iguais:
        return "Os números são iguais."
    else:
        return f"O maior número é {maior}."

def menorNumero():
    iguais = True
    qtd = int(input("Quantos números você deseja fornecer? "))

    for i in range(1, qtd + 1):
        num = float(input(f"Informe o {i}º número: "))

        if i == 1:
            aux = num
            menor = num
        elif num < menor:
            menor = num

        if aux != num:
            iguais = False
        aux = num

    if iguais:
        return "Os números são iguais."
    else:
        return f"O menor número é {menor}."

def main():
    while True:
        opcao = exibeOpcoes()

        if opcao == 1:
            print(maiorNumero())
        elif opcao == 2:
            print(menorNumero())
        elif opcao == 0:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

main()
