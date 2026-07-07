import time

class ViewHistoria:

    def __init__(self, Player, historia_dict):

        self.Player = Player
        self.historia_dict = historia_dict

    

    def print_historia(self):

        print(f"{self.historia_dict["historia"]}\n")

        continuar = input("Próximo -> ENTER / Sair -> Q : ")
        print()
        print()

        return continuar