import random

carro = random.randint(1, 3)


def escolha_usuario():
    while True:
        try:
            escolha = int(input("Escolha um numero entre 1 a 3 para encontrar o carro dourado: "))
            if escolha >= 4 or 0 >= escolha:
                print("Coloque um numero entre 1 a 3")
            else:
                return escolha
        except ValueError:
            print("Coloque um numero")



def escolha_apresentador():
    portas_escolhida = []
    portas = [1, 2, 3]
    for porta in portas:
        if porta != escolha and porta != carro:
            portas_escolhida.append(porta)
            return portas_escolhida


escolha = escolha_usuario()
porta_apresentador = escolha_apresentador()

print()
print(escolha)
print(carro)
print(porta_apresentador)

