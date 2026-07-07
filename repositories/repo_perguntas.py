import json

class RepoPerguntas:

    def __init__ (self, path):

        self.__path = path
        self.__perguntas_brutas_list = []
        
        self.__read_json()




    def __read_json(self):

        try :

            with open(self.__path , "r", encoding = "utf-8") as arquivo_json :

                self.__perguntas_brutas_list = json.load(arquivo_json)
                return self.__perguntas_brutas_list

                

        except FileNotFoundError:

            print(f"O arquivo {self.__path} não existe!!! ")
            self.__perguntas_brutas_list = []


    def get_perguntas_brutas(self):

        return self.__perguntas_brutas_list