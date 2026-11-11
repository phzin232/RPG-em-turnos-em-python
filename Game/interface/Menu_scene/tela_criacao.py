import customtkinter as ctk
from ...characters import player
from ...functions import generics 


class Criação(ctk.CTkFrame):
    def __init__(self, master, player_list, npc_list):
        super().__init__(master)

        self.master = master
        self.player_list = player_list
        self.npc_list = npc_list

        self.desenhat_tela()

    def Start_game(self):
        self.clear_windo()

        titulo = ctk.CTkLabel(self,text="Bem vindo ao RPG",font=("Arial", 30, "bold"),anchor="center")
        titulo.pack(pady=50)

        self.botao = ctk.CTkButton(self,text="aperta", command=self.start)
        self.botao.pack(pady=2)

    def start(self):
        self.clear_windo()

        self.label_criacao = ctk.CTkLabel(self, text="Crie seu personagem!",font=("arial",30,"bold"), anchor= "center")
        self.label_criacao.pack(pady=20)

        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Digite seu nome")
        self.entry_nome.pack(pady=20)

        self.bnt_confirmar = ctk.CTkButton(self, text="confirmar nome", command=self.confirmar_nome,hover=True)
        self.bnt_confirmar.pack(pady = 20)
    

    def confirmar_nome(self):
   
        nome = self.entry_nome.get()

        self.clear_windo()
        
        welcome = ctk.CTkLabel(self, text=f"então seu nome sera {nome}",font=("Arial", 30, "bold"))
        welcome.pack(pady = 50)
        playerst = player.gerar_player(nome)
        self.player_list.append(playerst)
        self.after(2000,self.iniciar_combate)
        