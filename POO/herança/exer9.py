class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar_motor(self):
        print(f"Motor de {self.potencia}cv ligado!")

    def exibir_info(self):
        print(f"Potência: {self.potencia}cv")


class Eletrico:
    def __init__(self, bateria):
        self.bateria = bateria

    def carregar(self):
        print(f"Carregando bateria de {self.bateria}kWh...")

    def exibir_info(self):
        print(f"Bateria: {self.bateria}kWh")


class Combustao:
    def __init__(self, tanque):
        self.tanque = tanque

    def abastecer(self):
        print(f"Abastecendo tanque de {self.tanque}L...")

    def exibir_info(self):
        print(f"Tanque: {self.tanque}L")


class CarroEletrico(Motor, Eletrico):
    def __init__(self, potencia, bateria):
        Motor.__init__(self, potencia)
        Eletrico.__init__(self, bateria)

    def exibir_info(self):
        print("--- Carro Elétrico ---")
        Motor.exibir_info(self)
        Eletrico.exibir_info(self)


class CarroHibrido(Motor, Eletrico, Combustao):
    def __init__(self, potencia, bateria, tanque):
        Motor.__init__(self, potencia)
        Eletrico.__init__(self, bateria)
        Combustao.__init__(self, tanque)

    def exibir_info(self):
        print("--- Carro Híbrido ---")
        Motor.exibir_info(self)
        Eletrico.exibir_info(self)
        Combustao.exibir_info(self)


ce = CarroEletrico(150, 75)
ce.exibir_info()
ce.ligar_motor()
ce.carregar()

print()

ch = CarroHibrido(200, 20, 50)
ch.exibir_info()
ch.ligar_motor()
ch.carregar()
ch.abastecer()