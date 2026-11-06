from random import randint, choices
from rich import print

class pStatus():
    def __init__(self, hp = 0, stamina = 0, name = " ",dano = 0):
        self.hp = hp
        self.hpmax = hp
        self.curou_nesta_rodada = False
        self.esquivou = False
        self.stamina = stamina
        self.staminamax = stamina
        
        self.name = name
        self.dano = dano
        
def gerar_player(name):
        hp = randint(200,350)
        stamina = randint(60,120)
        dano = randint(10,30)
        return pStatus(hp,stamina, name, dano)

def ataque_player(self, alvo):
     danomin = int(self.dano * 0.8)
     danomax = int(self.dano * 2)
     stamina = self.stamina

     dano = randint(danomin, danomax)

     bonus = int(stamina/3)

     chance_critico = 10 + bonus
     chance_normal = int(100 - chance_critico)

     tipo_dano = choices(["normal", "critico"], weights=[ chance_critico, chance_normal],k=1)[0]

     if tipo_dano == "critico":
          dano *= 3
          print(f"[yellow]CRITICO!")

     return dano

def cura(self):
        pocao = randint(20,50)
        self.hp += pocao
        if self.hp >= self.hpmax:
              cura_valida = pocao - (self.hp - self.hpmax)
              self.hp = self.hpmax
        else:
            cura_valida = pocao

        return cura_valida
