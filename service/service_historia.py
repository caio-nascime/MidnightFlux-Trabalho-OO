

class ServiceHistoria:

    def __init__(self, RepoHistoria, Player):

        self.RepoHistoria = RepoHistoria
        self.Player_obj= Player

        self.pos_json = Player.pos_json


    
    def verificar_tipo(self):

        tipo = self.RepoHistoria.get_tipo(self.pos_json)

        return tipo
    


    def carregar_parte(self):

        try:

            parte_historia_dict = self.RepoHistoria.get_historia_parte(self.pos_json)

            return parte_historia_dict
        
        except:

            print(" ERRO AO TENTAR ACESSAR O INDEX DA HISTORIA ")
            raise ValueError(" ERRO AO TENTAR ACESSAR O INDEX DA HISTORIA ")






if __name__ == "__main__" :

    ...