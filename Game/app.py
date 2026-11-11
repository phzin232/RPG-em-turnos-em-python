import customtkinter as ctk

from Game.interface.Menu_scene import tela_criacao



from rich.traceback import install
install()



class RPGApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("teste")

        self.player_list = []
        self.npc_list = []

        sel
        self.tela_criação = tela_criacao(self, self.player_list, self.npc_list)

        self.mostrar_tela(self.tela_criação)

    def mostar_tela(self, tela):
        self.tela_criação.pack_forget()
        self.tela_combate.pack_forget()

        tela.pack(fill="both", expand=True)
    def iniciar_combate(self):
        self.clear_windo()

        self.c_text = ctk.CTkLabel(self,text="Um Combate iniciara!",font=("Arial", 40, "bold"))
        self.c_text.pack(pady=20)







        





