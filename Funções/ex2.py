#   Construa um programa que manipule uma lâmpada. O programa deve exibir
# as seguintes opções ao usuário: (0)Sair; (1) Acender luz; (2) Apagar luz;
# (3) Consultar estado atual;

# Para isso o programa deve implementar as funções:
#  ▪ exibeOpcoes()
#    ▪ Escreve na tela o menu de opções.
#  ▪ acenderLampada()
#    ▪ Altera a lâmpada para acesa.
#  ▪ apagarLampada()
#    ▪ Altera a lâmpada para apagada.
#  ▪ exibirStatus()
#    ▪ Informa o estado atual da lâmpada.

def exibeMenu():
    print("##### MENU #####\n")
    print("(0) Sair\n")
    print("(1) Acender luz\n")
    print("(2) Apagar luz\n")
    print("(3) Consultar estado atual\n")
    opcao = int(input("Escolha uma opção: "))
    return opcao

def acenderLampada():
    return True  

def apagarLampada():
    return False  

def exibirStatus(estado):
    if estado:
        print("\nA lâmpada está ACESA.\n")
    else:
        print("\nA lâmpada está APAGADA.\n")

lampada = False  

while True:
    opcao = exibeMenu()

    if opcao == 0:
        print("\nEncerrando o programa...")
        break

    elif opcao == 1:
        if lampada:
            print("\nA lâmpada já está acesa!\n")
        else:
            lampada = acenderLampada()
            print("\nA lâmpada foi acesa.\n")

    elif opcao == 2:
        if lampada:
            lampada = apagarLampada()
            print("\nA lâmpada foi apagada.\n")
        else:
            print("\nA lâmpada já está apagada!\n")

    elif opcao == 3:
        exibirStatus(lampada)

    else:
        print("\nOpção inválida! Escolha um número entre 0 e 3.\n")

