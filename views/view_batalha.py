import os
import time

class ViewBatalha:

    def __init__(self, dict_player = None, dict_inimigo = None):

        self.dict_player = dict_player
        self.dict_inimigo = dict_inimigo

    


    def print_iniciar_batalha(self):
        
        os.system("cls" if os.name == "nt" else "clear")

        nome_jogador = self.dict_player["nome"]
        nome_inimigo = self.dict_inimigo["nome"]

        print("=" * 60)
        print("                      A BATALHA COMEÇOU")
        print("=" * 60)
        print("\n")

        
        print("        O  |===>                         __O=X")
        print("       /|\\                                 |  ")
        print("       / \\                                / \\ ")

        print("\n")
        print("-" * 60)

        print(f"      {nome_jogador} \t\t\t\t\t {nome_inimigo}")
        print("-" * 60)

        print("                     SE PREPARE ESTUDANTE\n\n")
        time.sleep(1)
        print("                     CARREGANDO PERGUNTAS...")

        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
        

    

    def ataque_inimigo_erro(self):

        
        nome_jogador = self.dict_player["nome"]
        vida_jogador = self.dict_player["vida"]
        # simbolo_vida_j = "[===...]"

        nome_inimigo = self.dict_inimigo["nome"]
        vida_inimigo = self.dict_inimigo["vida"]
        # simbolo_vida_i = "[=====.]"

        
        print("=" * 60)
        print("                  VOCÊ ERROU * O GOLPE CONECTOU! *")
        print("=" * 60)
        print("\n")

        
        print("          O       *POW!* __O=X ")
        print("        ~~/|\\_     \\|/                 |  ")
        print("         /  \\      / \\                / \\ ")

        print("\n")
        print("-" * 60)

       
        status_jogador = f"{nome_jogador}: {vida_jogador}HP"
        status_inimigo = f"{nome_inimigo}: {vida_inimigo}HP"

        
        print(f" {status_jogador:<35} {status_inimigo}")
        print("-" * 60)

        time.sleep(1.5)



    def ataque_inimigo_acerto(self):
        """O jogador acertou a pergunta na defesa e recebeu menos dano do inimigo (Defesa com Sucesso)"""
        nome_jogador = self.dict_player["nome"]
        vida_jogador = self.dict_player["vida"]
        nome_inimigo = self.dict_inimigo["nome"]
        vida_inimigo = self.dict_inimigo["vida"]

        print("=" * 60)
        print("          VOCÊ ACERTOU! * DEFESA BEM SUCEDIDA *")
        print("=" * 60)
        print("\n")

        # Representação gráfica: Jogador ergue a espada/escudo e o inimigo errou o golpe principal
        print("          O   |        __O=X ")
        print("        \\/|\\ /          |   \")")
        print("         / \\           / \\  \")")

        print("\n")
        print("-" * 60)
        status_jogador = f"{nome_jogador}: {vida_jogador}HP"
        status_limigo = f"{nome_inimigo}: {vida_inimigo}HP"
        print(f" {status_jogador:<35} {status_limigo}")
        print("-" * 60)
        time.sleep(1.5)




    def ataque_jogador_acerto(self):
        """O jogador acertou a pergunta no ataque e causou mais dano (Golpe Crítico)"""
        nome_jogador = self.dict_player["nome"]
        vida_jogador = self.dict_player["vida"]
        nome_inimigo = self.dict_inimigo["nome"]
        vida_inimigo = self.dict_inimigo["vida"]

        print("=" * 60)
        print("          VOCÊ ACERTOU! * GOLPE CRÍTICO CONECTADO! *")
        print("=" * 60)
        print("\n")

        # Representação gráfica: Jogador avança com a espada e acerta o inimigo (*CRASH!*)
        print("          O |===> *CRASH!* __O=X ")
        print("         /|\\       / //     _/    \")")
        print("         / \\       / \\      \\/    \")")

        print("\n")
        print("-" * 60)
        status_jogador = f"{nome_jogador}: {vida_jogador}HP"
        status_limigo = f"{nome_inimigo}: {vida_inimigo}HP"
        print(f" {status_jogador:<35} {status_limigo}")
        print("-" * 60)
        time.sleep(1.5)





    def ataque_jogador_erro(self):
        """O jogador errou a pergunta no ataque e causou menos dano (Golpe Fraco/Defendido)"""
        nome_jogador = self.dict_player["nome"]
        vida_jogador = self.dict_player["vida"]
        nome_inimigo = self.dict_inimigo["nome"]
        vida_inimigo = self.dict_inimigo["vida"]

        print("=" * 60)
        print("          VOCÊ ERROU! * O INIMIGO BLOQUEOU PARCIALMENTE *")
        print("=" * 60)
        print("\n")

        # Representação gráfica: A espada bate mas o inimigo se defende com o braço/arma
        print("          O  |==>X        __O=X ")
        print("         /|\\   /            |   \")")
        print("         / \\               / \\  \")")

        print("\n")
        print("-" * 60)
        status_jogador = f"{nome_jogador}: {vida_jogador}HP"
        status_limigo = f"{nome_inimigo}: {vida_inimigo}HP"
        print(f" {status_jogador:<35} {status_limigo}")
        print("-" * 60)
        time.sleep(1.5)



    def perguntar_usar_item(self, item):

        os.system("cls" if os.name == "nt" else "clear")

        print("=" * 60)
        print("                     ITEM DISPONÍVEL")
        print("=" * 60)
        print("\n")

        print(f"Nome: {item.nome}")
        print(f"Tipo: {item.__class__.__name__}")
        print(f"Observação: {item.observacao}")

        print("\n")
        print("-" * 60)

        resposta = input("Deseja utilizar este item? (s = sim / n = nao) : ")

        time.sleep(1.5)

        return resposta.lower() == "s"



    def mostrar_item_usado(self, item, player):

        print("=" * 60)
        print(f"                  VOCÊ CONSUMIU: {item.nome}")
        print("=" * 60)
        print("\n")

        print(f"Dano: {player.dano}")
        print(f"Vida: {player.vida}")

        print("\n")
        print("-" * 60)

        time.sleep(1.5)



    def vitoria(self):

        nome_jogador = self.dict_player["nome"]
        nome_inimigo = self.dict_inimigo["nome"]
        vida_jogador = self.dict_player["vida"]
        ira_jogador = self.dict_player["ira"]

        print("=" * 60)
        print("                    VOCÊ VENCEU A BATALHA!")
        print("=" * 60)
        print("\n")

        print("          \\O/                          x_x ")
        print("           |                            /|\\ ")
        print("          / \\                           / \\ ")

        print("\n")
        print("-" * 60)
        print(f"      {nome_jogador} \t\t\t\t\t {nome_inimigo}")
        print(f"      Vida: {vida_jogador}     Ira: {ira_jogador}")
        print("                     PARABÉNS, ESTUDANTE!")
        print("-" * 60)

        time.sleep(2)



    def derrota(self):

        nome_jogador = self.dict_player["nome"]
        nome_inimigo = self.dict_inimigo["nome"]
        vida_jogador = self.dict_player["vida"]
        ira_jogador = self.dict_player["ira"]

        print("=" * 60)
        print("                   VOCÊ FOI DERROTADO...")
        print("=" * 60)
        print("\n")

        print("          x_x                          \\O/ ")
        print("          /|\\                            |  ")
        print("          / \\                           / \\ ")

        print("\n")
        print("-" * 60)
        print(f"      {nome_jogador} \t\t\t\t\t {nome_inimigo}")
        print(f"      Vida: {vida_jogador}     Ira: {ira_jogador}")
        print("                     TENTE NOVAMENTE...")
        print("-" * 60)

        time.sleep(2)


