#   Adapte o programa do execício 2 para funcionar com 20 lâmpadas.
# Cada lâmpada será identificada por um número sequencial. Para
# acender, apagar, ou consultar o estado de uma lâmpada será necessário
# informar o identificador da lâmpada desejada.

# ▪ Para isso o programa deve implementar as funções:
#  ▪ exibeOpcoes()
#    ▪ Escreve na tela o menu de opções.
#  ▪ acenderLampada(int idLampada)
#    ▪ Altera a lâmpada para acesa.
#  ▪ apagarLampada(int idLampada)
#    ▪ Altera a lâmpada para apagada.
#  ▪ exibirStatus(int idLampada)
#    ▪ Informa o estado atual da lâmpada.
#  ▪ exibirTodas()
#    ▪ Informa o estado atual de todas as lâmpadas.

def exibeMenu():
    print("\n##### MENU #####\n")
    print("(0) Sair\n")
    print("(1) Acender luz\n")
    print("(2) Apagar luz\n")
    print("(3) Consultar estado de uma lâmpada\n")
    print("(4) Consultar todas as lâmpadas\n")
    return int(input("Escolha uma opção: "))

def acenderLampada(lampadas):
    idLampada = int(input("\nInforme o ID da lâmpada que deseja acender (1 a 20): "))
    if 1 <= idLampada <= 20:
        if lampadas[idLampada - 1]:
            print(f"\nA lâmpada {idLampada} já está acesa.")
        else:
            lampadas[idLampada - 1] = True
            print(f"\nA lâmpada {idLampada} foi acesa.")
    else:
        print("ID inválido! Escolha um número entre 1 e 20.")

def apagarLampada(lampadas):
    idLampada = int(input("\nInforme o ID da lâmpada que deseja apagar (1 a 20): "))
    if 1 <= idLampada <= 20:
        if lampadas[idLampada - 1]:
            lampadas[idLampada - 1] = False
            print(f"\nA lâmpada {idLampada} foi apagada.")
        else:
            print(f"\nA lâmpada {idLampada} já está apagada.")
    else:
        print("ID inválido! Escolha um número entre 1 e 20.")

def exibirStatus(lampadas):
    idLampada = int(input("\nInforme o ID da lâmpada que deseja saber o estado atual (1 a 20): "))
    if 1 <= idLampada <= 20:
        estado = "acesa" if lampadas[idLampada - 1] else "apagada"
        print(f"\nA lâmpada {idLampada} está {estado}.")
    else:
        print("ID inválido! Escolha um número entre 1 e 20.")

def exibirTodas(lampadas):
    for i in range(len(lampadas)):
        estado = "ACESA" if lampadas[i] else "APAGADA"
        print(f"\nLâmpada {i + 1}: {estado}")

num_lampadas = 20
lampadas = [False] * num_lampadas

while True:
    opcao = exibeMenu()

    if opcao == 0:
        print("\nEncerrando o programa...")
        break
    elif opcao == 1:
        acenderLampada(lampadas)
    elif opcao == 2:
        apagarLampada(lampadas)
    elif opcao == 3:
        exibirStatus(lampadas)
    elif opcao == 4:
        exibirTodas(lampadas)
    else:
        print("\nOpção inválida! Escolha um número entre 0 e 4.")
