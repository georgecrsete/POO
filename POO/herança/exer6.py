class Nadador:
    def mover(self):
        print("Nadando...")

class Corredor:
    def mover(self):
        print("Correndo...")

class Triatleta(Nadador, Corredor):
    def mover(self):
        Nadador.mover(self)
        Corredor.mover(self)
        print("Eu sou Triatleta")

t1 = Triatleta()
t1.mover()