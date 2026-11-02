from random import randint, choices,choice
from rich import print

class nStatus():
    def __init__(self, hp = 0, stamina = 0, name = "", tipo_npc = "", dano = 0): 
        self.hp = hp
        self.hpmax = hp
        self.stamina = stamina
        self.staminamax = stamina
        self.name = name
        self.tipo_npc = tipo_npc
        self.dano = dano

class Monstro(nStatus):
    def __init__(self, hp = 0, stamina = 0, name = "", tipo_npc = "", dano = 0):
        super().__init__(hp, stamina, name, tipo_npc, dano)
        self.hotil = True

class NPCamigavel(nStatus):
    def __init__(self, hp = 0, stamina = 0, name = "", tipo_npc = "", dano = 0):
        super().__init__(hp, stamina, name, tipo_npc, dano)
        self.hotil = False
        self.dialogo = True

def gerar_monstro():
    hp = randint(10,50)
    dano = randint(3,10)
    stamina = randint(10,120)

    tipo_npc = choices(["Goblin", "Orc", "Wolf", "Demon", "Fallen Angel"], weights=[40, 20, 30,9,1],k=1)[0]
    name = f"{tipo_npc} {choice(["Avançado", "Novo", "Batedor"])}"
    if tipo_npc == "Goblin":
        stamina /= 1.3
        hp *= 1.02
        dano /=1.20
    if tipo_npc == "Orc":
        hp *=2
        stamina /= 2
        dano *= 2
    if tipo_npc == "Wolf":
        hp /= 1.2
        stamina *= 4
        dano *= 1.5
    if tipo_npc == "Demon":
        hp *= 15
        stamina *= 25
        dano *=3
    if tipo_npc == "Fallen Angel":
        hp *= 130
        stamina *= 1160
        dano = randint(10,15)
        dano *=5
    return nStatus( int(hp), int(stamina), name, tipo_npc, int(dano))

def npc_ataque(self, alvo):
    tipo_npc = self.tipo_npc
    dano = self.dano
    tipo_dano = ""

    if tipo_npc == "Goblin":
        tipo_dano = choices(["normal", "critico"], weights=[ 90,10],k=1)[0]
        if tipo_dano == "critico":
            dano = int(dano * 1.5)

    elif tipo_npc == "Orc":
        tipo_dano = choices(["normal", "critico"], weights=[ 90,10],k=1)[0]
        if tipo_dano == "critico":
            dano = int(dano * 2)

    elif tipo_npc == "Wolf":
        tipo_dano = choices(["normal", "critico"], weights=[ 90,10],k=1)[0]
        if tipo_dano == "critico":
            dano = int(dano * 1.3)


    elif tipo_npc == "Demon":
        tipo_dano = choices(["normal", "critico"], weights=[ 90,10],k=1)[0]
        if tipo_dano == "critico":
            dano = int(dano * 3)
                
    elif tipo_npc == "Fallen Angel":
        tipo_dano = choices(["normal", "critico"], weights=[ 90,10],k=1)[0]
        if tipo_dano == "critico":
            dano = int(dano * 6)

    if tipo_dano == "critico":
        print(f"[red]CRITICO!\n")


    return dano 
