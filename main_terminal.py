from Game.characters import npc
from Game.characters import player
from Game.functions import attack
from Game.functions import  generics
from rich import print, inspect
from rich.traceback import install
from random import choices
from rich.panel import Panel
import time


install()
player_list = []
npc_list = []


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

def start(buff):
    game_started = False
    status = "waiting"
    listvalidar = ["sim","s"]
    ask = generics.validar("Gostaria de iniciar?\n",listvalidar )
    
    if ask in ["s", "sim"]:
        name = input("Nome por favor!\n")
        playerst = player.gerar_player(name)
        player_list.append(playerst)
        print(detail(playerst))
        game_started = True
        time.sleep(3)
        generics.gerar_horda(status, game_started, npc_list, player_list, atacar,buff)

    elif ask in ["mais", "+", "dois"]:
        monterst = npc.gerar_monstro()
        npc_list.append(monterst)
        print(detail(monterst))
        print("feito")

def novo_jogo():
    player_list.clear()
    npc_list.clear()
    listvalidar = ["sim", "não"]
    ask = generics.validar(f"Gostaria de começar um novo jogo? Sim ou não?\n",listvalidar)
    if ask == "não":
        print(f"[purple] obrigado por jogar!\n")
        quit()
    if ask == "sim":
        start()

def end(status):
   if status == "game over":
        print(f"[red]Game Over")
        time.sleep(3)
        player_list.clear()
        npc_list.clear()
        novo_jogo()

def turno_montro(ordemdeataque):
    turno = ordemdeataque[0]
    custa_esquiva = 15
    
    if player_list[0].stamina >= custa_esquiva:
        lista_esquiva_valida = ["sim","nao","não","esquivar","esquiva","s","e","n","d","desviar"]
        ask_esquiva = generics.validar(f"\nO {turno.name} irá te atacar! gostaria de [blue]desviar?[/]", lista_esquiva_valida )

        if ask_esquiva.startswith(("s","e","d")) :
            if player_list[0].stamina < custa_esquiva:
                print(f"\nestamina necessaria: {custa_esquiva} estamina disponivel: {player_list[0].stamina}")

            else:
                player_list[0].stamina -= custa_esquiva
                print(f"Você gastou [blue]15 de estamina [/]e esta com [blue]{player_list[0].stamina}") 
                player_list[0].esquivou = True 

                if player_list[0].stamina < 0:
                    player_list[0].stamina = 0 

                return

    dano = npc.npc_ataque(turno, player_list[0])

    if player_list[0].stamina < custa_esquiva :
        print(f"estamina abaixo de 15! [red bold]esquiva indisponivel dano aumentado.[/]")
        ask_esquiva = "nao"
        dano = int(dano * 1.80)

             
    if  ask_esquiva.startswith(("n")):

        print(f"\nO monstro {turno.name} ira te atacar com: {dano} de dano \n"
                "Agora você tem\n")
            
        player_list[0].hp -= dano
        player_list[0].esquivou = False



        time.sleep(1.5)
    
def turno_player(ordemdeataque,inimigos):

    ordemdeataque[0]

    funcao_escolhida = generics.validar_acao("\nO que gostaria de fazer?\n [red]Cura[/] [blue]atacar[/]",acoes_plataque)

    alvo, dano = funcao_escolhida(ordemdeataque, inimigos, player_list[0])
    player_list[0].esquivou = False

    return alvo, dano

def atacar(status, inimigos, ordemdeataque):
    if status == "ready" or status == "combate":
        turno = ordemdeataque[0]
        dano = 0
        status = "combate"

        if len(inimigos) > 0 and isinstance(turno, npc.nStatus):
            turno_montro(ordemdeataque)

            if player_list[0].hp > 0:

                print(detail(player_list[0]))
                ordemdeataque.append(ordemdeataque.pop(0))
                time.sleep(3)

            elif player_list[0].hp <= 0:
                print(f"\nO monstro {turno.name} te matou com {dano} de dano!\n")
                status = "game over"
                end(status)
                return

            contador = 1
            for cabacice in ordemdeataque:
                print(f"{contador} - {cabacice.name}(HP:{cabacice.hp})\n")
                contador += 1        

        elif len(inimigos) > 0 and isinstance(turno, player.pStatus):
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
            print("Você Ganhou essa rodada!")
            listvalidos = ["s", "sim"," n", "não"]
            ask = generics.validar(f"gostaria de continuar? uma nova horda sera gerada!\n"
                             "e você ganhara buffs!",listvalidos)
            if ask.startswith("s"):
                progresso(status)
            elif ask.startswith("n"):
                return novo_jogo()

def progresso(status):
        buffplayer = choices([1.2, 2], k=1)[0]
        buffenemie = choices([1.5, 3],k=1)[0]

        player_list[0].hpmax = int(player_list[0].hpmax * buffplayer)
        player_list[0].staminamax = int(player_list[0].staminamax * buffplayer)
        player_list[0].dano = int(player_list[0].dano * buffplayer)

        player_list[0].stamina = player_list[0].staminamax
        qtd_curadap = player.cura(player_list[0]) = player.cura(player_list[0])
        if  player_list.hp >=  player_list.hpmax :
            print(f"\nVida ja está no maximo!")

        qtd_curadap = player.cura( player_list)
        print(f"\nVocê [red]foi curado em {qtd_curadap} parabêns!")


        
        generics.gerar_horda(status, True, npc_list, player_list, atacar,buffenemie)


acoes_plataque = {
    "atacar": attack.player_ataque,
    "cura" : attack.player_cura
}

start(buff=0)
