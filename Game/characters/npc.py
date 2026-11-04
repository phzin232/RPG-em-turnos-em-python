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

monster_database = {
    "Goblin":   {"hp_mult":  1.2, "stamina_mult": 1.3, "dano_mult":  0.8},
    "Orc":   {"hp_mult":  2, "stamina_mult": 0.5, "dano_mult":  2},
    "Wolf":   {"hp_mult":  0.8, "stamina_mult": 4, "dano_mult":  1.5},
    "Demon":   {"hp_mult":  15, "stamina_mult": 25, "dano_mult":  3},
    "Fallen Angel":   {"hp_mult":  130, "stamina_mult": 1160, "dano_mult":  6},

    }

def gerar_monstro():
    hp = randint(100,500)
    dano = randint(3,10)
    stamina = randint(10,120)

    tipo_npc = choices(["Goblin", "Orc", "Wolf", "Demon", "Fallen Angel"], weights=[40, 20, 30,9,1],k=1)[0]

    rules = monster_database.get(tipo_npc)

    final_damage = dano * rules["dano_mult"]
    final_hp = hp * rules["hp_mult"]
    final_stamina = stamina * rules["stamina_mult"] 

    name = f"{tipo_npc} {choice(["Avançado", "Novo", "Batedor"])}"



    return nStatus( int(final_hp), int(final_stamina), name, tipo_npc, int(final_damage))

def npc_ataque(self, player):
    tipo_npc = self.tipo_npc
    dano = self.dano

    table_monster = {
        "Goblin":   {"chance_critico": 100, "multiplicador": 1.5},
        "Orc":    {"chance_critico": 99, "multiplicador": 2},
        "Wolf":     {"chance_critico": 98, "multiplicador": 1.3},
        "Demon":    {"chance_critico": 97, "multiplicador": 3},
        "Fallen Angel":     {"chance_critico": 96, "multiplicador": 6}
    }

    regras = table_monster.get(tipo_npc, {"chance_critico":10, "multiplicador": 2})

    chance_normal = 100 - regras["chance_critico"]
    critical_chance = regras ["chance_critico"]
    multipliyer = regras["multiplicador"]

    tipo_dano = choices(["normal","critico"],weights=[chance_normal,critical_chance],k=1)[0]

    if tipo_dano == "critico" and player[0].esquivou == False:
        print(f"[yellow]CRITÍCO!")
        dano = int(dano * multipliyer)

    return dano
