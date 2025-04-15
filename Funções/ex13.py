#   Escreva uma função que recebe um inteiro positivo m e devolve 1 se m é
# primo, 0 em caso contrário. Escreva uma função main que utiliza a função
# implementada.

def eh_primo(m):
    if m < 2:
        return 0  
    
    for i in range(2, m): 
        if m % i == 0:
            return 0 

    return 1

def main():
    m = int(input("Digite um número inteiro positivo: "))
    
    if eh_primo(m):
        print(f"{m} é um número primo.")
    else:
        print(f"{m} não é um número primo.")

main()
