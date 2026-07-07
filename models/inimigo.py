import random


class Inimigo:

    def __init__(self, nome, vida, dano, inventario, dificuldade, disciplina):

        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.inventario = inventario
        self.dificuldade = dificuldade
        self.disciplina = disciplina





    def atacar(self, acerto):


        print("estou atacando")

        if acerto :

            fator_random = (random.randint(0 , 5))/10

            dano = self.dano * fator_random

            print(f"Estou dando {dano} de dano")

            return dano
        

        else :

            fator_random = (random.randint(5 , 15))/10

            dano = self.dano * fator_random

            print(f"Estou dando {dano} de dano")

            return dano



    def receber_dano(self, dano):

        print(f"estou recebendo {dano} de dano")

        vida = self.vida - dano

        return vida
    

