from models.player import Player

class ViewMenu:

    def __init__(self):

        self.player = None 


    def criar_player(self):

        print("Bem vindo ao jogo BLA BLA BLA")
        nome = input("Como podemos te chamar, calouro? : ")

        return nome
    


    def usuario_criado(self, nome):

        print(f"Agora sim, {nome}! Agora você faz parte da FCTE, está devidamente matriculado")
    

    

    def bem_vindo_novamente(self, player_obj):

        print(f"Bem vindo de volta {player_obj.nome}\nVocê está atualmente com {player_obj.vida}\nBLA BLA BLA")
