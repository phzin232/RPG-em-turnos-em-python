import time
from Game.characters import player
from Game.characters import npc
from rich import print



def player_cura(ordemdeataque, inimigos, player_list):
    if  player_list.curou_nesta_rodada :
        print(f"\nVocê já se curou nessa rodada!")
        ordemdeataque.append(ordemdeataque.pop(0))

    elif  player_list.hp >=  player_list[0].hpmax :
        print(f"\nVida ja está no maximo!")
        ordemdeataque.append(ordemdeataque.pop(0))

    else:
        qtd_curadap = player.cura( player_list[0])
        print(f"\nVocê [red]curou {qtd_curadap} parabêns!")

        
    return None, 0

def player_ataque(ordemdeataque, inimigos,  player_list):
        print(f"\nLista de quem atacar!\n")
        contador = 1
        for cabacice in inimigos:
            if isinstance (cabacice,npc.nStatus):
                print(f"{contador} - {cabacice.name}(HP:{cabacice.hp})\n")
                contador += 1
        time.sleep(0.5)
        alvo_escolha = int(input(f"Escolha quem atacar! digite o numero correspondente.\n")) - 1

        while alvo_escolha  >= len(inimigos) or alvo_escolha  < 0:
            print("Digite um numero valido por favor!\n")
            alvo_escolha  = int(input(f"Escolha quem atacar! digite o numero correspondente.\n")) - 1


        alvo = inimigos[alvo_escolha ]
        dano = player.ataque_player(player_list, alvo)
        alvo.hp -= dano
        player_list.curou_nesta_rodada = False

        return alvo, dano 
