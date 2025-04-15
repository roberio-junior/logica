#   Construa um programa que solicita o total gasto pelo cliente de uma loja,
# imprime as opções de pagamento, solicita a opção desejada e imprime o valor
# total das prestações (se houverem).

#   1) Opção: a vista com 10% de desconto
#   2) Opção: em duas vezes (preço da etiqueta)
#   3) Opção: de 3 até 10 vezes com 3% de juros ao mês (somente para
#   compras acima de R$100,00).

# OBS: Implemente uma função que imprime as opções, solicita a opção
# desejada e retorna a opção escolhida. Na função principal verifique a
# opção escolhida e invoque a função correspondente (uma função para cada
# opção).

def exibeOpcoes():
    print("\nEscolha a opção de pagamento:")
    print("1 - À vista com 10% de desconto")
    print("2 - Em duas vezes (preço normal)")
    print("3 - De 3 até 10 vezes com 3% de juros ao mês (para compras acima de R$100,00)")
    
    opcao = int(input("Digite a opção desejada: "))
    return opcao

def pagamento_a_vista(total):
    return total * 0.9

def pagamento_duas_vezes(total):
    return total / 2 

def pagamento_parcelado(total):
    if total < 100:
        return "Parcelamento disponível apenas para compras acima de R$100,00."

    parcelas = int(input("Escolha o número de parcelas (de 3 a 10): "))
    
    if parcelas < 3 or parcelas > 10:
        return "Número de parcelas inválido. Escolha entre 3 e 10."

    valor_final = total * (1 + 0.03 * parcelas)
    valor_parcela = valor_final / parcelas

    return f"Total com juros: R${valor_final:.2f} | {parcelas}x de R${valor_parcela:.2f}"

def main():
    total = float(input("Digite o total gasto pelo cliente: R$"))
    
    opcao = exibeOpcoes()
    
    if opcao == 1:
        print(f"Total a pagar à vista: R${pagamento_a_vista(total):.2f}")
    elif opcao == 2:
        print(f"Total a pagar em duas vezes: 2x de R${pagamento_duas_vezes(total):.2f}")
    elif opcao == 3:
        print(pagamento_parcelado(total))
    else:
        print("Opção inválida! Reinicie o programa e tente novamente.")

    print("\nEncerrando o programa...")

main()


