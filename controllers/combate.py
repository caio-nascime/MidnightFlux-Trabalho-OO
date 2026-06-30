from service.service_perguntas import ServicePerguntas
from service.service_motor_combate import MotorCombate
from service.service_user import ServiceUser

from repositories.repo_perguntas import RepoPerguntas
from repositories.repo_player import RepoPlayer

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

                    print("parabens vc ganhou")
                    
                    player = service_user.atualizar_pos_json(dict_historia["proximo"])
                    return player

                else :

                    print("LOSSEEEERRRR")
                    #Volto para o texto anterior
                    player = service_user.retornar_pos_json(dict_historia["anterior"])
                    return player

            else :

                continue




if __name__ == "__main__" :

    ...