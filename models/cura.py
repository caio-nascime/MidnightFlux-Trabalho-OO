from models.item import Item


class Cura(Item):

    def __init__(self, nome, observacao, valor_cura):

        self.nome = nome
        self.observacao = observacao
        self.valor_cura = valor_cura


    def usar_item(self, player):

        player.vida += self.valor_cura

        return player
