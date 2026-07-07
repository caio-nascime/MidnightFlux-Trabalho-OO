from models.player import Player
import time
import os


class ViewMenu:

    def __init__(self):

        self.player = None 

        self.midnight = [
    "███╗   ███╗██╗██████╗ ███╗  ██╗██╗ ██████╗ ██╗  ██╗████████╗",
    "████╗ ████║██║██╔══██╗████╗ ██║██║██╔════╝ ██║  ██║╚══██╔══╝",
    "██╔████╔██║██║██║  ██║██╔██╗██║██║██║  ███╗███████║   ██║   ",
    "██║╚██╔╝██║██║██║  ██║██║╚████║██║██║   ██║██╔══██║   ██║   ",
    "██║ ╚═╝ ██║██║██████╔╝██║ ╚███║██║╚██████╔╝██║  ██║   ██║   ",
    "╚═╝     ╚═╝╚═╝╚═════╝ ╚═╝  ╚══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ",
]
 
        self.flux = [
    "███████╗██╗     ██╗   ██╗██╗  ██╗",
    "██╔════╝██║     ██║   ██║╚██╗██╔╝",
    "█████╗  ██║     ██║   ██║ ╚███╔╝ ",
    "██╔══╝  ██║     ██║   ██║ ██╔██╗ ",
    "██║     ███████╗╚██████╔╝██╔╝ ██╗",
    "╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝",
]


    def criar_player(self):
        print()

        print("                       BEM VINDO AO")
        print()
        for linha in self.midnight:
            print(linha)

        for linha in self.flux:
            print(linha)

        print()

        time.sleep(1.5)

        nome = input("       COMO PODEMOS TE CHAMAR CALOURO? : ")

        print()

        return nome
    
    


    def usuario_criado(self, nome):

        print(f"\nAgora sim, {nome}! Agora você faz parte da FCTE, está devidamente matriculado")

        time.sleep(1.5)

        os.system("cls" if os.name == "nt" else "clear")
    

    

    def bem_vindo_novamente(self, player_obj):


        print()

        print(f"\n                 BEM VINDO DE VOLTA AO ")

        print()


        for linha in self.midnight:
            print(linha)

        for linha in self.flux:
            print(linha)

        time.sleep(1)

        print()

        print(f"{player_obj.nome}, você está atualmente com {player_obj.vida} de vida.\n  TOME CUIDADO, A FCTE PRECISA DE VOCÊ\n")

        time.sleep(2.5)

        print("LOADING...\n\n")
        

        time.sleep(2)

        print("CARREGANDO PACOTES...")

        time.sleep(2)

        os.system("cls" if os.name == "nt" else "clear")

    


    def despedida(self, Player):

        print(f"Até logo {Player.nome}! Descansar que o homem não é de ferro !")
        print(f"Atualmente você está com {Player.vida} de vida e {Player.vida}, se recupere para amnhanhã, não vá para o HH\n\n")

