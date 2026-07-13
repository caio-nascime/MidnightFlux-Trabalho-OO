from models.item import Item

class Buff(Item):

    def __init__(self, nome, observacao, valor_buff):

        self.nome = nome
        self.observacao = observacao
        self.valor_buff = valor_buff


    def usar_item(self, player):

        player.dano += self.valor_buff

        return player
