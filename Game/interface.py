import customtkinter as ctk



class RPGApp(ctk.CTk):
    def __init__(self, ):
        super().__init__()
        self.geometry("800x600")
        self.title("teste")

    def Start_game(self, start):
        self.clear_windo()
        titulo = ctk.CTkLabel(self,text="Bem vindo ao RPG",font=("Arial", 30, "bold"))
        titulo.pack(pady=50)
        self.botao = ctk.CTkButton(self,text="aperta", command=start)
        self.botao.pack(pady=20)


    def clear_windo(self):
        for widget in self.winfo_children():
            widget.destroy()












app = RPGApp()
app.mainloop()