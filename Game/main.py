from characters.npc import nStatus, gerar_monstro, npc_ataque
from characters.player import pStatus, gerar_player, ataque_player, cura
from rich import print, inspect
from rich.traceback import install
from random import randint, shuffle
from rich.panel import Panel
import time

install()
player = []
npc = []


def validar(pergunta, lista):
    print(f"{pergunta}")
    text_a_validar = input(" ").strip().lower()

    while text_a_validar  not in lista:
        text_a_validar = input("Digite novamente por gentileza!\n").strip().lower()
    return text_a_validar

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
        gerar_horda(status, game_started)

    elif ask in ["mais", "+", "dois"]:
        monterst = gerar_monstro()
        npc.append(monterst)
        print(detail(monterst))
        print("feito")

def novo_jogo():
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

def gerar_horda(status,game_started):
    if game_started == True:
       
        status = "preparing"
        global quantia_montro 
        quantia_montro = randint(1,7)
        while quantia_montro > 0:
            monterst = gerar_monstro()
            npc.append(monterst)
            quantia_montro -= 1    
       
        quantia_montro = len(npc)
        ordem(status)
    else:
        print("Valide o codigo primeiro. Erro fatal.")

def ordem(status):
    ordemataque = []
    if status == "preparing":
        if quantia_montro >=1:
                shuffle(npc)
        ordemataque.extend(player)
        ordemataque.extend(npc)
        shuffle(ordemataque)

        status = "ready"
        numerar_inimigos(status, ordemataque)

def numerar_inimigos(status, ordemataque):
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
        
def atacar(status, inimigos, ordemdeataque):
    if status == "ready" or status == "combate":
        turno = ordemdeataque[0]
        dano = 0
        status = "combate"

        if len(inimigos) > 0 and isinstance(turno, nStatus):

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
                        ordemdeataque.append(ordemdeataque.pop(0))    

                        if player[0].stamina <0:
                            player[0].stamina = 0 

            dano = npc_ataque(turno,player[0])

            if player[0].stamina < custa_esquiva :
                print(f"estamina abaixo de 15! [red bold]esquiva indisponivel dano aumentado.[/]")
                ask_esquiva = "nao"
                dano = int(dano * 1.80)

                
                
            if  ask_esquiva == "não" or ask_esquiva == "nao":

                print(f"\nO monstro {turno.name} ira te atacar com: {dano} de dano \n"
                      "Agora você tem\n")
                    
                player[0].hp -= dano
                time.sleep(1.5)

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

            ask = validar(("\nO que gostaria de fazer?\n [red]Cura[/] [blue]atacar[/]"), ["cura", "atacar"])
        
            if ask == "cura":
                if player[0].curou_nesta_rodada :
                    print(f"\nVocê já se curou nessa rodada!")
                    ask = "atacar"

                elif player[0].hp >= player[0].hpmax :
                    print(f"\nVida ja está no maximo!")
                    ordemdeataque.append(ordemdeataque.pop(0))


                else:
                    qtd_curadap = cura(player[0])
                    print(f"\nVocê [red]curou {qtd_curadap} parabêns!")
                    player[0].curou_nesta_rodada = True
                    ordemdeataque.append(ordemdeataque.pop(0))


            elif ask == "atacar":
                print(f"\nLista de quem atacar!\n")
                contador = 1
                for cabacice in inimigos:
                    if isinstance (cabacice,nStatus):
                        print(f"{contador} - {cabacice.name}(HP:{cabacice.hp})\n")
                        contador += 1
                time.sleep(0.5)
                alvo_escolha = int(input(f"Escolha quem atacar! digite o numero correspondente.\n")) - 1

                while alvo_escolha  >= len(inimigos) or alvo_escolha  < 0:
                    print("Digite um numero valido por favor!\n")
                    alvo_escolha  = int(input(f"Escolha quem atacar! digite o numero correspondente.\n")) - 1


                alvo = inimigos[alvo_escolha ]
                dano = ataque_player(player[0],alvo)
                alvo.hp -= dano
                player[0].curou_nesta_rodada = False

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



start()