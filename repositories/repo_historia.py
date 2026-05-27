import json

class RepoHistoria:

    def __init__ (self, path):

        self.__path = path
        self.__historia_list = []
        
        self.read_json()




    def read_json(self):

        try :

            with open(self.__path , "r", encoding = "utf-8") as arquivo_json :

                self.__historia_list = json.load(arquivo_json)
                return self.__historia_list

                

        except FileNotFoundError:

            print(f"O arquivo {self.__path} não existe!!! ")
            self.__historia_list = []




    def get_historia_list(self):
        return self.__historia_list
    


    

    def get_historia_parte(self, pos_json):
        return self.__historia_list[pos_json]
    


    

    def get_tipo(self, pos_json):
        
        return self.__historia_list[pos_json]["tipo"]
    



    def get_falas_acerto(self, pos_json):


        return self.__historia_list[pos_json]["inimigo"]["falas_acerto"]
    



    def get_falas_erro(self, pos_json):


        return self.__historia_list[pos_json]["inimigo"]["falas_erro"]
    



    




if __name__ == "__main__" :

    repo_player = RepoHistoria('database/historia.json')
    json_carregado = repo_player.get_historia_list()
    print(json_carregado)
    print(type(json_carregado))