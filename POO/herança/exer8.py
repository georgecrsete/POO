class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar(self):
        print(f"Motor de {self.potencia}cv ligado!")


class MotorEletrico(Motor):
    def __init__(self, potencia, autonomia):
        super().__init__(potencia)
        self.autonomia = autonomia

    def ligar(self):
        print(f"Motor elétrico de {self.potencia}cv ligado! Autonomia: {self.autonomia}km")


class Carro:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor  

    def ligar(self):
        print(f"Carro {self.marca} ligando...")
        self.motor.ligar()


class CarroEletrico(Carro):
    def __init__(self, marca, motor_eletrico):
        super().__init__(marca, motor_eletrico)  

    def ligar(self):
        print(f"Carro elétrico {self.marca} ligando...")
        self.motor.ligar()


motor_comum = Motor(150)
carro = Carro("Toyota", motor_comum)
carro.ligar()

print()

motor_ev = MotorEletrico(200, 400)
ev = CarroEletrico("Tesla", motor_ev)
ev.ligar()
