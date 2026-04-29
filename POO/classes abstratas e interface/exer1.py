from abc import ABC, abstractmethod

class Controlavel(ABC):
    @abstractmethod
    def mover(self):
        pass

class Jogador(Controlavel):
    def mover(self):
        print("jogador se movendo")

class Volante(Controlavel):
    def mover(self):
        print("volante girando")



b = Jogador()
b.mover()

c = Volante()
c.mover()