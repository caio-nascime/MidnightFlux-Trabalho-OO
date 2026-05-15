from service.service_user import ServiceUser
from service.service_historia import ServiceHistoria

from repositories.repo_player import RepoPlayer
from repositories.repo_historia import RepoHistoria

from views.view_menu import ViewMenu
from views.view_historia import ViewHistoria




class Sistema():

    def __init__(self) :

        self.player = None
        self.inimigo = None
        self.perguntas = [] 
        self.proresso = None
        self.service_user =  None



    
    def iniciar(self):

        player = self.carregar_player()

        self.player = player

        self.loop_principal()

    




    def carregar_player(self, flag = True):

        self.service_user = ServiceUser(RepoPlayer('database/player.json'))
        nome_player = self.service_user.buscar_nome()


        if nome_player == "None":

            nome = ViewMenu().criar_player()
            self.service_user.criar_player(nome)

            return self.carregar_player(False)

        else:

            player = self.service_user.carregar_player()

            if flag :

                ViewMenu().bem_vindo_novamente(player)

            else :

                ViewMenu().usuario_criado(nome_player)

            return player




    def loop_principal(self) :
         
        

        while True:

            service_historia = ServiceHistoria(RepoHistoria("database/historia.json"), self.player)
             
            tipo = service_historia.verificar_tipo()

            parte_historia_dict = service_historia.carregar_parte()


            if tipo == "texto" :

                print_parte = ViewHistoria(self.player, parte_historia_dict) # Não estou usando o player por enquanto

                continuar = print_parte.print_historia()


                if continuar == "":
                    
                    self.player = self.service_user.atualizar_pos_json(parte_historia_dict["proximo"]) # CORRIGIR ESTA FUNCIONALIDADE, NÃO ESTA TROCANDO DE JSON / POSIÇÃO
                

                elif continuar.lower() == "q" or continuar.lower() == "quit" or continuar.lower() == "sair":
                    break                         # FAZER A LÓGICA CASO O USUÁRIO QUEIRA SAIR 
                

                else:
                    ... #CRIAR LÓGICA



            






if __name__ == "__main__" :

    Sistema().iniciar()
