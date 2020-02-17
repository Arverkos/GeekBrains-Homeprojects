from abc import ABC, abstractmethod


class Cloth(ABC):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @abstractmethod
    def textile(self):
        pass


class Coat(Cloth):

    @property
    def textile(self):
        return self.size / 6.5 + 0.5


class Suit(Cloth):

    @property
    def textile(self):
        return 2 * self.size + 0.3


cloth_1 = Suit('Костюм', 4)

print(cloth_1.textile)
