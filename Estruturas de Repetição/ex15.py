#   Tendo em vista o alto preço da gasolina, os motoristas estão
# preocupados com a quilometragem percorrida por seus automóveis. Um
# motorista fez o controle recompletando várias vezes o tanque e
# registrando os quilômetros percorridos e os litros de gasolina
# necessários para encher o tanque. Desenvolva um programa em Python
# que receba como dados a quilometragem dirigida e os litros usados
# para recompletar o tanque. O programa deve calcular e exibir a
# quilometragem por litro obtida para cada recompletamento. Depois de
# processar todas as informações, o programa deve calcular e exibir a
# média de quilômetros por litro obtida para todos os recompletamentos.

total_km = 0
total_litros = 0
contador = 0

while True:
    litros = float(input("Entre com os litros consumidos (-1 para finalizar): "))
    
    if litros == -1:
        break
    
    km = float(input("Entre com os km percorridos: "))
    
    km_por_litro = km / litros
    print(f"A taxa km/litro para esse tanque foi: {km_por_litro:.2f}km/l")
    
    total_km += km
    total_litros += litros
    contador += 1

if contador > 0:
    media_km_por_litro = total_km / total_litros
    print(f"\nA taxa toral de km/litro foi: {media_km_por_litro:.2f}km/l")
else:
    print("Nenhum dado foi registrado.")
