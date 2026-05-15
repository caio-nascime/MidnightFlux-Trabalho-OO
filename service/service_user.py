from repositories.repo_player import RepoPlayer
from models.player import Player




class ServiceUser():

    def __init__(self, RepoPlayer):

        self.RepoPlayer = RepoPlayer





    def buscar_nome(self) :

        dict_player = self.RepoPlayer.get_infos_player()

        return dict_player["nome"]

        # if jogador.nome == "None":




    def carregar_player(self):

        dict_infos_player = self.RepoPlayer.get_infos_player()

        player = Player(dict_infos_player["nome"], dict_infos_player["vida"], dict_infos_player["ira"], dict_infos_player["inventario"], dict_infos_player["pos_historia"])

        return player
    



    def criar_player(self, nome):

        self.RepoPlayer.criar_player(nome)
    


    def atualizar_pos_json(self, prox_pos):

        self.RepoPlayer.atualizar_pos_json(prox_pos)

        player = self.carregar_player()

        return player
            

        

            
    
