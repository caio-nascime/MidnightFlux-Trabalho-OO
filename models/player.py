

class Player:

    def __init__(self, nome, vida, ira, inventario, pos_json):

        self.__nome = nome
        self.vida = vida
        self.ira = ira
        self.inventario = inventario
        self.__pos_json = pos_json


    @property
    def nome(self):
        return self.__nome
    



    @property
    def pos_json(self):
        return self.__pos_json

