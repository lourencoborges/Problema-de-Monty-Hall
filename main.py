import random

carro = random.randint(1, 3)
portas_escolhida = []
portas = [1, 2, 3]
contagem_vitoria = 0
contagem_derrota = 0


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
    for porta in portas:
        if porta != escolha and porta != carro:
            portas_escolhida.append(porta)
    porta_selecionada = random.choice(portas_escolhida)
    return portas_escolhida, porta_selecionada

    
def segunda_escolha():
    portas_copia = [1, 2, 3]
    portas_copia.remove(porta_selecionada)
    portas_copia.remove(escolha)
    trocar_porta = portas_copia[0]
    return trocar_porta

def decisao_usuario():
    while True:
        try:
            escolha_usuario_2 = input("Voce quer trocar de porta? (s/n)")
            escolha_final = escolha_usuario_2.lower()
            if escolha_final == "s" or escolha_final == "n":
                return escolha_final
            else:
                print("Bote apenas (s/n)")
        except ValueError:
            print("Bote apenas (s/n)")
        

def porta_final():
    if escolha_final == "s":
        ultima_porta = trocar_porta
    elif escolha_final == "n":
        ultima_porta = escolha
    return ultima_porta

def verificar_vitoria():
    global contagem_vitoria
    global contagem_derrota
    if ultima_porta == carro:
        print("Parabens, voce ganhou")
        contagem_vitoria += 1
    else:
        print("Que pena, voce perdeu")
        contagem_derrota += 1



escolha = escolha_usuario()

portas_escolhida, porta_selecionada = escolha_apresentador()

trocar_porta = segunda_escolha()

escolha_final = decisao_usuario()

ultima_porta = porta_final()

verificar_vitoria()
