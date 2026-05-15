import json
from models.player import Player

class RepoPlayer():

    def __init__ (self, path):

        self.__path = path
        self.__infos_player = None
        self.__read_json()


    def __read_json(self):

        try :

            with open(self.__path , "r", encoding = "utf-8") as arquivo_json :

                self.__infos_player = json.load(arquivo_json)
                return self.__infos_player

                

        except FileNotFoundError:

            print(f"O arquivo {self.__path} não existe!!! ")
            self.__infos_player = None




    def get_infos_player(self):
        return self.__infos_player
    



    def criar_player(self , nome):

        self.__infos_player["nome"] = nome

        with open(self.__path , 'w', encoding= 'utf-8') as arquivo_json:
            json.dump(self.__infos_player, arquivo_json, indent=4, ensure_ascii=False)


    

    def atualizar_pos_json(self, prox_pos):

        self.__infos_player["pos_historia"] = prox_pos

        with open(self.__path , 'w', encoding= 'utf-8') as arquivo_json:
            json.dump(self.__infos_player, arquivo_json, indent=4, ensure_ascii=False)




if __name__ == "__main__" :

    repo_player = RepoPlayer('database/player.json')
    json_carregado = repo_player.carregar_player()
    print(json_carregado)
    print(type(json_carregado))