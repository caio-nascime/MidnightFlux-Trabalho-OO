from repositories.repo_player import RepoPlayer
from models.player import Player
from models.cura import Cura
from models.buff import Buff




class ServiceUser():

    def __init__(self, RepoPlayer):

        self.RepoPlayer = RepoPlayer





    def buscar_nome(self) :

        dict_player = self.RepoPlayer.get_infos_player()

        return dict_player["nome"]

        # if jogador.nome == "None":




    def carregar_player(self):

        dict_infos_player = self.RepoPlayer.get_infos_player()

        inventario = []

        for item_dict in dict_infos_player["inventario"]:

            if item_dict["tipo"] == "Cura":

                inventario.append(Cura(item_dict["nome"], item_dict["observacao"], item_dict["valor_cura"]))

            elif item_dict["tipo"] == "Buff":

                inventario.append(Buff(item_dict["nome"], item_dict["observacao"], item_dict["valor_buff"]))

        player = Player(dict_infos_player["nome"], dict_infos_player["vida"], dict_infos_player["dano"] , dict_infos_player["ira"], inventario, dict_infos_player["pos_historia"])

        return player
    



    def criar_player(self, nome):

        self.RepoPlayer.criar_player(nome)
    


    def atualizar_pos_json(self, prox_pos):

        self.RepoPlayer.atualizar_pos_json(prox_pos)

        player = self.carregar_player()

        return player
    



    def retornar_pos_json(self, pos_anterior):

        self.RepoPlayer.atualizar_pos_json(pos_anterior)
        player = self.carregar_player()

        return player




    def atualizar_player(self, player):

        lista_inventario = []

        for item in player.inventario:

            if isinstance(item, Cura):

                lista_inventario.append({"tipo" : "Cura", "nome" : item.nome, "observacao" : item.observacao, "valor_cura" : item.valor_cura})

            elif isinstance(item, Buff):

                lista_inventario.append({"tipo" : "Buff", "nome" : item.nome, "observacao" : item.observacao, "valor_buff" : item.valor_buff})

        self.RepoPlayer.atualizar_player(player.nome, player.vida, player.dano, player.ira, lista_inventario, player.pos_json)

        

            
    
