#   Escreva um programa que leia um inteiro não-negativo n e imprima a
# soma dos n primeiros números primos. Escreva uma função main que utiliza
# za função implementada.

def eh_primo(m):
    if m < 2:
        return False
    
    for i in range(2, m):
        if m % i == 0:
            return False 
    
    return True

def soma_n_primos(n):
    soma = 0
    contador = 0
    numero = 2
    
    while contador < n:
        if eh_primo(numero):
            soma += numero
            contador += 1
        numero += 1
    
    return soma

def main():
    n = int(input("Digite um número inteiro não-negativo: "))
    
    if n < 0:
        print("Por favor, digite um número não-negativo.")
    else:
        print(f"A soma dos {n} primeiros números primos é: {soma_n_primos(n)}")

main()
