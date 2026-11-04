from rich import print
import time
from random import randint, shuffle
from characters.npc import gerar_monstro, nStatus



def validar(pergunta, lista):
    print(f"{pergunta}")
    text_a_validar = input(" ").strip().lower()

    while text_a_validar  not in lista:
        text_a_validar = input("Digite novamente por gentileza!\n").strip().lower()
    return text_a_validar

def validar_acao(pergunta, dict_a_ser_verificada):
    print(f"{pergunta}")

    while True:
        ask = input(f" ").strip().lower()
        funcao_escolhida = None

        for letras in dict_a_ser_verificada.keys():
            if letras.startswith(ask):
                funcao_escolhida = dict_a_ser_verificada[letras]
                break
        if funcao_escolhida:
            return funcao_escolhida
        else:
            print(f"Função não localizada tente novamente!")

def gerar_horda(status,game_started, npc, player, atacar):
    if game_started == True:
       
        status = "preparing"
        global quantia_montro 
        quantia_montro = randint(1,10)
        while quantia_montro > 0:
            monterst = gerar_monstro()
            npc.append(monterst)
            quantia_montro -= 1    
       
        quantia_montro = len(npc)
        ordem(status,player, npc, atacar)
    else:
        print("Valide o codigo primeiro. Erro fatal.")

def ordem(status, player, npc, atacar):
    ordemataque = []
    if status == "preparing":
        if quantia_montro >=1:
                shuffle(npc)
        ordemataque.extend(player)
        ordemataque.extend(npc)
        shuffle(ordemataque)

        status = "ready"
        numerar_inimigos(status, ordemataque, atacar)

def numerar_inimigos(status, ordemataque, atacar):
    contador = 1
    inimigos = []
    if status == "ready":
        print(f"A ordem do combate é:\n")
        for cabacice in ordemataque:
                print(f"{contador} - {cabacice.name}(HP:{cabacice.hp})")
                contador += 1
        time.sleep(3)
        print(f"\nJá a de inimigos sem você é:")
        contador = 1
        for cabacice in ordemataque:
            if isinstance(cabacice, nStatus):
                print(f"{contador} - {cabacice.name}(HP:{cabacice.hp})")
                contador += 1
                inimigos.append(cabacice)
        atacar(status, inimigos, ordemataque)

