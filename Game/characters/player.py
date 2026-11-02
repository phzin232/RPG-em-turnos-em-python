from random import randint, choices
from rich import print

class pStatus():
    def __init__(self, hp = 0, stamina = 0, name = " ",dano = 0):
        self.hp = hp
        self.hpmax = hp
        self.curou_nesta_rodada = False
        self.stamina = stamina
        self.staminamax = stamina
        self.name = name
        self.dano = dano
        
def gerar_player():
        name = input("Nome por favor!\n")
        hp = randint(50,100)
        stamina = randint(10,120)
        dano = randint(8,20)
        return pStatus(hp,stamina, name, dano)

def ataque_player(self, alvo):
     dano = self.dano
     min_critico = 50
     max_critico = 50
     tipo_dano = choices(["normal", "critico"], weights=[ max_critico, min_critico],k=1)[0]
     if tipo_dano == "critico":
          dano *= 3
          print(f"[yellow]CRITICO!")
     return dano

def cura(self):
        pocao = randint(10,30)
        self.hp += pocao
        if self.hp >= self.hpmax:
              cura_valida = pocao - (self.hp - self.hpmax)
              self.hp = self.hpmax
        else:
            cura_valida = pocao

        return cura_valida
        
        




