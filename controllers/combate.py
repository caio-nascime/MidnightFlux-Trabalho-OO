import random

from service.service_perguntas import ServicePerguntas
from service.service_motor_combate import MotorCombate
from service.service_user import ServiceUser

from repositories.repo_perguntas import RepoPerguntas
from repositories.repo_player import RepoPlayer

from models.cura import Cura
from models.buff import Buff
from models.player import Player

from views.view_batalha import ViewBatalha



class Combate:

    def __init__(self, Player, Inimigo):

        self.Player = Player
        self.Inimigo = Inimigo

        # self.Disciplina = self.carregar_disciplina(self.Inimigo.disciplina)
        self.lista_perguntas = self.__carregar_perguntas(self.Inimigo.disciplina)

        self.jogador_copy = {"nome" : self.Player.nome, "vida" : self.Player.vida, "ira" : self.Player.ira, "dano" : self.Player.dano, "inventario" : self.Player.inventario, "combo" : 0}

        self.inimigo_copy = {"nome" : self.Inimigo.nome, "vida" : self.Inimigo.vida, "dano" : self.Inimigo.dano, "inventario" : self.Inimigo.inventario, "dificuldade" : self.Inimigo.dificuldade, "disciplina" : self.Inimigo.disciplina}

        # def carregar_disciplina(self, disciplina):

        #     disciplina_obj = Disc





    def __carregar_perguntas(self, disciplina):

        path_perguntas = "database/perguntas_" + disciplina + ".json"

        repo_perguntas = RepoPerguntas(path_perguntas)

        service_perguntas = ServicePerguntas(repo_perguntas)

        perguntas = service_perguntas.carregar_perguntas(self.Inimigo.dificuldade)

        self.lista_perguntas = perguntas

        return self.lista_perguntas
    
    


    def __sortear_item(self):

        num_sorteado = random.randint(0,10)

        if num_sorteado >= 3 and num_sorteado < 7:

            novo_item = Cura("DinDin da Tia", "Restaura 10 pontos de vida", 10)

            return novo_item

        elif num_sorteado >= 7:

            novo_item = Buff("Suco do RU", "Aumenta o dano do próximo ataque", 10)

            return novo_item

        else:

            return None

    




    def verificar_fim(self):

        if self.inimigo_copy["vida"] <= 0 :

            return [True , "ganhou"]
        
        elif self.jogador_copy["vida"] <= 0 :

            return [True , "Perdeu"]
        
        else:

            return [False]







    def turno(self, dict_historia):

        service_user = ServiceUser(RepoPlayer('database/player.json'))
         
        round = 0 
        combo = 0 
        ja_feitas = []

        view_batalha = ViewBatalha(self.jogador_copy, self.inimigo_copy)

        view_batalha.print_iniciar_batalha()
         
        while True :

            motor_combate = MotorCombate(self.jogador_copy, self.inimigo_copy, self.lista_perguntas, round)
            
            if round % 2 == 0: #Se o round for par é do player

                list_result_inimigo = motor_combate.turno_player(combo)

                self.inimigo_copy = list_result_inimigo[0]

                if list_result_inimigo[1] == 1:

                    combo += 1

                else:

                    combo = 0

                print(f"Combo : {combo}")

                round += 1


            else:

                #Vai chamar motor_combate.turno_inimigo()
                #E atualizar o dict do player 
                
                list_result_player = motor_combate.turno_inimigo(combo)

                self.jogador_copy = list_result_player[0]

                if list_result_player[1] == 1:

                    combo += 1

                else:

                    combo = 0

                print(f"Combo : {combo}")

                round += 1


            list_fim = self.verificar_fim()

            if list_fim[0] :

                if list_fim[1] == "ganhou":

                    service_user.atualizar_pos_json(dict_historia["proximo"])

                    item_sorteado = self.__sortear_item()

                    if item_sorteado:

                        self.jogador_copy["inventario"].append(item_sorteado)

                        print(f"Você ganhou: {item_sorteado.nome}!")

                    player = Player(self.jogador_copy["nome"], self.jogador_copy["vida"], self.jogador_copy["dano"], self.jogador_copy["ira"], self.jogador_copy["inventario"], dict_historia["proximo"])

                    player.ganhar_ira()

                    view_batalha_atualizada = ViewBatalha({"nome" : player.nome, "vida" : player.vida, "ira" : player.ira}, self.inimigo_copy)

                    view_batalha_atualizada.vitoria()


                    service_user.atualizar_player(player)

                    return player

                else :

                    #Volto para o texto anterior
                    service_user.retornar_pos_json(dict_historia["anterior"])

                    player = Player(self.jogador_copy["nome"], self.Player.vida, self.jogador_copy["dano"], self.jogador_copy["ira"], self.jogador_copy["inventario"], dict_historia["anterior"])

                    player.perder_vida_derrota()

                    player.perder_ira()

                    view_batalha_atualizada = ViewBatalha({"nome" : player.nome, "vida" : player.vida, "ira" : player.ira}, self.inimigo_copy)

                    view_batalha_atualizada.derrota()

                    service_user.atualizar_player(player)

                    return player

            else :

                continue




if __name__ == "__main__" :

    ...