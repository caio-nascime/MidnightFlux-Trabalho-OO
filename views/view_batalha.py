import os

class ViewBatalha:

    def __init__(self, dict_player = None, dict_inimigo = None):

        self.dict_player = dict_player
        self.dict_inimigo = dict_inimigo

    


    def print_iniciar_batalha(self):
        
        os.system("cls" if os.name == "nt" else "clear")

        print(" A BATALHA INICIOU !! ")



    