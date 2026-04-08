# Classe Motor
class Motor:
    
    # construtor
    def __init__(self, potencia):
        self.potencia = potencia   # potência do motor em cavalos

    # método para ligar o motor
    def ligar(self):
         print(f"Motor de {self.potencia} cavalos ligado.")


# Classe Carro
class Carro:
    
    # construtor recebe um motor já existente (agregação)
    def __init__(self, modelo, motor):
        self.modelo = modelo   # modelo do carro
        self.motor = motor     # objeto Motor associado ao carro

    # método para ligar o carro
    def ligar(self):
        print(f"Ligando o {self.modelo}")  # mostra o modelo
        
        # chama o método ligar do objeto Motor
        self.motor.ligar()
    

# criação do motor
motor1 = Motor(170)

# criação do carro recebendo o motor
carro1 = Carro("Celta", motor1)

# ligando o carro (que liga o motor também)
carro1.ligar()