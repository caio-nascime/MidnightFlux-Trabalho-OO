from repositories.repo_perguntas import RepoPerguntas

class ServicePerguntas:

    def __init__(self, RepoPerguntas):

        self.RepoPerguntas = RepoPerguntas


    def carregar_perguntas(self, dificuldade):

        perguntas_brutas_list = self.RepoPerguntas.get_perguntas_brutas()

        return perguntas_brutas_list[ dificuldade - 1 ]