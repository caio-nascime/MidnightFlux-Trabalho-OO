import random

from models.player import Player
from models.inimigo import Inimigo

from views.view_pergunta import ViewPergunta
from views.view_batalha import ViewBatalha


class MotorCombate:

    def __init__(self, jogador, inimigo, perguntas, round):

        self.jogador_dict = jogador 
        self.inimigo_dict = inimigo
        self.perguntas_list = perguntas

        self.round = round


    

    def sortear_pergunta(self):


        index_pergunta = random.randint(0, len(self.perguntas_list ) - 1)

        pergunta = self.perguntas_list[index_pergunta]

        return pergunta
    




    def turno_player(self, combo):

        pergunta_dict = self.sortear_pergunta()

        view_pergunta = ViewPergunta(pergunta_dict)

        while True:

            resposta = view_pergunta.print_pergunta("player")

            if resposta in ["a", "b", "c", "d"]:

                break

            else :

                print("\nResposta inválida marque uma das 4 alternativas : \n")

        
        
        player  = Player(self.jogador_dict["nome"], self.jogador_dict["vida"],self.jogador_dict["dano"], self.jogador_dict["ira"], self.jogador_dict["inventario"], self.jogador_dict["combo"])
        inimigo = Inimigo(self.inimigo_dict["nome"], self.inimigo_dict["vida"], self.inimigo_dict["dano"], self.inimigo_dict["inventario"], self.inimigo_dict["dificuldade"], self.inimigo_dict["disciplina"])

        view_batalha = ViewBatalha(self.jogador_dict, self.inimigo_dict)
        

        if resposta == pergunta_dict["correta"]:
            ...
            #instancia jogador com o dict
            # Chama o ataque da classe jogador -> Jogador.ataque(True)
            #Preciso retornar o dict -> [dict_jogador , 1]

            dano = player.atacar(True)

            new_vida = inimigo.receber_dano(dano)

            self.inimigo_dict["vida"] = new_vida
            
            view_batalha.ataque_jogador_acerto()

            return [self.inimigo_dict , 1]  #soma mais um no combo

        else:
            ... 
            # Chama o ataque da classe jogador -> Jogador.ataque(False)
            #Preciso retornar o dict -> [dict_jogador , 0]

            dano = player.atacar(False)

            new_vida = inimigo.receber_dano(dano)

            self.inimigo_dict["vida"] = new_vida

            view_batalha.ataque_jogador_erro()

            return [self.inimigo_dict , 0] # Zera o combo





    def turno_inimigo(self, combo):

        pergunta_dict = self.sortear_pergunta()

        view_pergunta = ViewPergunta(pergunta_dict)

        while True:

            resposta = view_pergunta.print_pergunta("inimigo")

            if resposta in ["a", "b", "c", "d"]:

                break

            else :

                print("\nResposta inválida marque uma das 4 alternativas : \n")

        
        
        player = Player(self.jogador_dict["nome"], self.jogador_dict["vida"],self.jogador_dict["dano"], self.jogador_dict["ira"], self.jogador_dict["inventario"], self.jogador_dict["combo"])
        inimigo = Inimigo(self.inimigo_dict["nome"], self.inimigo_dict["vida"], self.inimigo_dict["dano"], self.inimigo_dict["inventario"], self.inimigo_dict["dificuldade"], self.inimigo_dict["disciplina"])

        view_batalha = ViewBatalha(self.jogador_dict, self.inimigo_dict)


        if resposta == pergunta_dict["correta"]:
    
            #instancia jogador com o dict
            # Chama o ataque da classe jogador -> Jogador.ataque(True)
            #Preciso retornar o dict -> [dict_jogador , 1]

            dano = inimigo.atacar(True)

            new_vida = player.receber_dano(dano)

            self.jogador_dict["vida"] = new_vida

            view_batalha.ataque_inimigo_acerto()

            return [self.jogador_dict , 1]  #soma mais um no combo


        else:
        
            # Chama o ataque da classe jogador -> Jogador.ataque(False)
            #Preciso retornar o dict -> [dict_jogador , 0]

            dano = inimigo.atacar(False)

            new_vida = player.receber_dano(dano)

            self.jogador_dict["vida"] = new_vida

            
            view_batalha.ataque_inimigo_erro()


            return [self.jogador_dict , 0] # Zera o combo