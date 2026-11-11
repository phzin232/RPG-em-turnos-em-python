from rich import print
import time
from random import randint, shuffle
from Game.characters import npc



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

def gerar_horda(status, game_started, npc_list, player, atacar):
    if game_started == True:
       
        status = "preparing"
        global quantia_montro 
        quantia_montro = randint(1,1)
        while quantia_montro > 0:
            monterst = npc.gerar_monstro()
            npc_list.append(monterst)
            quantia_montro -= 1    
       
        quantia_montro = len(npc_list)
        ordem(status,player, npc_list, atacar)
    else:
        print("Valide o codigo primeiro. Erro fatal.")

def ordem(status, player_list,npc_list, atacar):
    ordemataque = []
    if status == "preparing":
        if quantia_montro >=1:
                shuffle(npc_list)
        ordemataque.extend(player_list)               
        ordemataque.extend(npc_list)

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
            if isinstance(cabacice, npc.nStatus):
                print(f"{contador} - {cabacice.name}(HP:{cabacice.hp})")
                contador += 1
                inimigos.append(cabacice)
        atacar(status, inimigos, ordemataque)

