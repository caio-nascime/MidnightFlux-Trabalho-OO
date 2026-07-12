from abc import ABC, abstractmethod


class Item(ABC):

    @abstractmethod
    def usar_item(self, player):
        ...
