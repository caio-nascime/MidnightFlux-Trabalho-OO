import random

class Player:

    def __init__(self, nome, vida, dano, ira, inventario, pos_json):

        self.__nome = nome
        self.vida = vida
        self.dano = dano
        self.ira = ira
        self.inventario = inventario
        self.__pos_json = pos_json


    @property
    def nome(self):
        return self.__nome
    



    @property
    def pos_json(self):
        return self.__pos_json





    def atacar(self, acerto):

        

        if acerto :

            fator_random = (random.randint(5, 15))/100

            dano = self.dano * self.ira * fator_random

            print(f"Estou dando {dano} de dano")

            return dano
        

        else :

            fator_random = (random.randint(0 , 5))/100

            dano = self.dano * self.ira * fator_random

            return dano
            



    def receber_dano(self, dano):

        vida = self.vida - dano

        return vida



    def perder_ira(self):

        self.ira = max(self.ira - 0.75, 0)

        return self.ira



    def ganhar_ira(self):

        if self.ira < 5:

            self.ira = min(self.ira + 0.5, 5)

        return self.ira



    def perder_vida_derrota(self):

        self.vida -= 5

        return self.vida