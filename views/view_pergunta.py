import os

class ViewPergunta:

    def __init__(self, pergunta):

        self.pergunta_dict = pergunta




    def _linha(self, tamanho=60, caractere="-"):

        return caractere * tamanho
    



    def print_pergunta(self, player_inimigo):

        os.system("cls" if os.name == "nt" else "clear")

        pergunta = self.pergunta_dict

        enunciado = pergunta.get("Enunciado", "Pergunta indisponível")
        alternativas = [
            ("A", pergunta.get("a", "")),
            ("B", pergunta.get("b", "")),
            ("C", pergunta.get("c", "")),
            ("D", pergunta.get("d", "")),
        ]

        print()
        print(self._linha())
        if player_inimigo == "player":

            print("|" + " VÁ PARA CIMA, ATAQUE !! ".center(58) + "|")

        else :
            print("|" + " ACERTE PARA SE DEFENDER !! ".center(58) + "|")

        print(self._linha())
        print()
        print(f"Enunciado: {enunciado.strip()}")
        print()
        print("Alternativas:")

        for letra, texto in alternativas:
            print(f"  [{letra}] {texto.strip()}")

        print()
        print(self._linha())
        resposta = input("Digite A, B, C ou D para responder : ").lower()
        print()
        print(self._linha())
        print()

        return resposta




if __name__ == "__main__":

    pergunta = ViewPergunta({"Enunciado" : "Como crio uma função ? ", 
"a" : "func Ola(pedro) ",
"b" : "def Ola(pedro) ",
"c" : "definir Ola(pedro) ",
"d" : "funcao Ola(pedro)",
"correta" : "b"})
    
    pergunta.print_pergunta()