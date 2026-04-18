# ============================================================
# EXERCÍCIO 8 - Herança + Composição
# Conceito: Além da herança (é um), usamos composição (tem um).
#           Carro TEM UM Motor — isso é composição.
#           MotorEletrico É UM Motor — isso é herança.
# ============================================================

# --- HIERARQUIA DOS MOTORES ---

# Classe PAI — motor genérico
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia  # Potência em cavalos (cv)

    def ligar(self):
        print(f"Motor de {self.potencia}cv ligado!")


# Classe FILHA — motor elétrico herda de Motor e adiciona autonomia
class MotorEletrico(Motor):
    def __init__(self, potencia, autonomia):
        super().__init__(potencia)     # Reaproveita o atributo potencia
        self.autonomia = autonomia     # Km que pode percorrer com carga cheia

    def ligar(self):
        # Sobrescreve o ligar() com informações adicionais
        print(f"Motor elétrico de {self.potencia}cv ligado! Autonomia: {self.autonomia}km")


# --- HIERARQUIA DOS CARROS ---

# Classe Carro — usa COMPOSIÇÃO: recebe um objeto Motor como atributo
class Carro:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor  # Composição: Carro TEM UM Motor

    def ligar(self):
        print(f"Carro {self.marca} ligando...")
        self.motor.ligar()  # Delega a ação de ligar ao motor interno


# Classe CarroEletrico herda de Carro e recebe um MotorEletrico
class CarroEletrico(Carro):
    def __init__(self, marca, motor_eletrico):
        super().__init__(marca, motor_eletrico)  # Passa o motor elétrico para Carro

    def ligar(self):
        print(f"Carro elétrico {self.marca} ligando...")
        self.motor.ligar()  # Chama o ligar() do MotorEletrico


# --- Testando ---

motor_comum = Motor(150)
carro = Carro("Toyota", motor_comum)
carro.ligar()
# Saída:
# Carro Toyota ligando...
# Motor de 150cv ligado!

print()

motor_ev = MotorEletrico(200, 400)
ev = CarroEletrico("Tesla", motor_ev)
ev.ligar()
# Saída:
# Carro elétrico Tesla ligando...
# Motor elétrico de 200cv ligado! Autonomia: 400km
