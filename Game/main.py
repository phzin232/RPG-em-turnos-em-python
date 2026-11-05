from characters.npc import nStatus, gerar_monstro, npc_ataque
from characters.player import pStatus, gerar_player
from functions.attack import player_cura, player_ataque
from functions.generics import validar_acao, validar, gerar_horda
from rich import print, inspect
from rich.traceback import install
from random import randint, shuffle
from rich.panel import Panel
import time


install()
player = []
npc = []



def detail(personagem):
    conteudo = (
        f"[bold blue]Nome:[/]{personagem.name}\n" 
        f"[bold red]HP: [/]{personagem.hp}\n"
        f"[bold cyan]Estamina:[/]{personagem.stamina}\n"
     )

    return Panel(conteudo,
                 expand=False,
                 title=f"{personagem.name}",
                 border_style="red"
                 )

def start():
    game_started = False
    status = "waiting"
    listvalidar = ["player","um","mais","+","dois"]
    ask = validar("Gostaria de criar um Player ou mais de um?\n",listvalidar )
    
    
    if ask in ["player", "um"]:
        playerst = gerar_player()
        player.append(playerst)
        print(detail(playerst))
        game_started = True
        time.sleep(3)
        gerar_horda(status, game_started, npc, player, atacar)

    elif ask in ["mais", "+", "dois"]:
        monterst = gerar_monstro()
        npc.append(monterst)
        print(detail(monterst))
        print("feito")

def novo_jogo():
    player.clear()
    npc.clear()
    listvalidar = ["sim", "não"]
    ask = validar(f"Gostaria de começar um novo jogo? Sim ou não?\n",listvalidar)
    if ask == "não":
        print(f"[purple] obrigado por jogar!\n")
        quit()
    if ask == "sim":
        start()

def end(status):
   if status == "game over":
        print(f"[red]Game Over")
        time.sleep(3)
        player.clear()
        npc.clear()
        novo_jogo()

def turno_montro(ordemdeataque):
    turno = ordemdeataque[0]
    custa_esquiva = 15
    if player[0].stamina >= custa_esquiva:
        lista_esquiva_valida = ["sim","nao","não","esquivar","esquiva","s","e","n","d","desviar"]
        ask_esquiva = validar(f"\nO {turno.name} irá te atacar! gostaria de [blue]desviar?[/]", lista_esquiva_valida )

        if ask_esquiva.startswith(("s","e","d")) :
            if player[0].stamina < custa_esquiva:
                print(f"\nestamina necessaria: {custa_esquiva} estamina disponivel: {player[0].stamina}")

            else:
                player[0].stamina -= custa_esquiva
                print(f"Você gastou [blue]15 de estamina [/]e esta com [blue]{player[0].stamina}") 
                player[0].esquivou = True 

                if player[0].stamina < 0:
                    player[0].stamina = 0 

                return

    dano = npc_ataque(turno, player)

    if player[0].stamina < custa_esquiva :
        print(f"estamina abaixo de 15! [red bold]esquiva indisponivel dano aumentado.[/]")
        ask_esquiva = "nao"
        dano = int(dano * 1.80)

             
    if  ask_esquiva.startswith(("n")):

        print(f"\nO monstro {turno.name} ira te atacar com: {dano} de dano \n"
                "Agora você tem\n")
            
        player[0].hp -= dano
        player[0].esquivou = False



        time.sleep(1.5)
    
def turno_player(ordemdeataque,inimigos):

    ordemdeataque[0]

    funcao_escolhida = validar_acao("\nO que gostaria de fazer?\n [red]Cura[/] [blue]atacar[/]",acoes_plataque)

    alvo, dano = funcao_escolhida(ordemdeataque, inimigos, player)
    player[0].esquivou = False

    return alvo, dano

def atacar(status, inimigos, ordemdeataque):
    if status == "ready" or status == "combate":
        turno = ordemdeataque[0]
        dano = 0
        status = "combate"

        if len(inimigos) > 0 and isinstance(turno, nStatus):
            turno_montro(ordemdeataque)

            if player[0].hp > 0:

                print(detail(player[0]))
                ordemdeataque.append(ordemdeataque.pop(0))
                time.sleep(3)

            elif player[0].hp <= 0:
                print(f"\nO monstro {turno.name} te matou com {dano} de dano!\n")
                status = "game over"
                end(status)
                return

            contador = 1
            for cabacice in ordemdeataque:
                print(f"{contador} - {cabacice.name}(HP:{cabacice.hp})\n")
                contador += 1        

        elif len(inimigos) > 0 and isinstance(turno, pStatus):
            alvo, dano = turno_player(ordemdeataque,inimigos)

            if alvo is not None:
                if alvo.hp > 0:

                    print(f"O {alvo.name} sofreu {dano} de dano!\n"
                        f"vida do {alvo.name} está {alvo.hp}\n")
                    time.sleep(3)
                    ordemdeataque.append(ordemdeataque.pop(0))

                elif alvo.hp <= 0:
                    print(f"O {alvo.name} morreu!\n")
                    ordemdeataque.remove(alvo)
                    inimigos.remove(alvo)
            
        if len(inimigos) > 0:
            atacar(status,inimigos,ordemdeataque)

        elif len(inimigos) == 0:
            print("FIM DE JOGO GANHOU")
            return novo_jogo()

acoes_plataque = {
    "atacar": player_ataque,
    "cura" : player_cura
}


start()