class Computador():
    def __init__(self, processador, memoria):
        self.processador = processador
        self.memoria = memoria

class Laptop(Computador):
    def __init__(self, processador, memoria, bateriawatts = 0):
        super().__init__(processador, memoria)
        self.bateriawatts = bateria_watts


class Desktop(Computador):
    def __init__(self, processador, memoria, gabinete = ''):    
        super().__init__(processador, memoria)
        self.gabinete = gabinete


notebook2 = Laptop("AMD Ryzen 7", 16, 65)
print(notebook2.bateria_watts)


pc = Desktop("Intel i9", 32)
print(pc.processador)
print(pc.gabinete) 


pc2 = Desktop("Intel i9", 32, "ATX Tower")
print(pc2.gabinete)