# ============================================================
# EXERCÍCIO 9 - Herança Múltipla Avançada (Mixin Pattern)
# Conceito: Classes independentes (Motor, Eletrico, Combustao) são
#           combinadas via herança múltipla para formar veículos complexos
# ============================================================

# --- CLASSES BASE (independentes entre si) ---

# Representa o motor mecânico
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia  # Potência em cv

    def ligar_motor(self):
        print(f"Motor de {self.potencia}cv ligado!")

    def exibir_info(self):
        print(f"Potência: {self.potencia}cv")


# Representa o sistema elétrico (bateria)
class Eletrico:
    def __init__(self, bateria):
        self.bateria = bateria  # Capacidade em kWh

    def carregar(self):
        print(f"Carregando bateria de {self.bateria}kWh...")

    def exibir_info(self):
        print(f"Bateria: {self.bateria}kWh")


# Representa o sistema de combustão (tanque)
class Combustao:
    def __init__(self, tanque):
        self.tanque = tanque  # Capacidade do tanque em litros

    def abastecer(self):
        print(f"Abastecendo tanque de {self.tanque}L...")

    def exibir_info(self):
        print(f"Tanque: {self.tanque}L")


# --- CLASSES COMPOSTAS POR HERANÇA MÚLTIPLA ---

# Carro elétrico: herda de Motor e Eletrico
class CarroEletrico(Motor, Eletrico):
    def __init__(self, potencia, bateria):
        # Como há herança múltipla, chamamos cada __init__ diretamente
        # (em vez de super(), que seguiria o MRO e poderia pular algum)
        Motor.__init__(self, potencia)
        Eletrico.__init__(self, bateria)

    def exibir_info(self):
        print("--- Carro Elétrico ---")
        Motor.exibir_info(self)    # Exibe info do motor
        Eletrico.exibir_info(self) # Exibe info da bateria


# Carro híbrido: herda de Motor, Eletrico E Combustao
class CarroHibrido(Motor, Eletrico, Combustao):
    def __init__(self, potencia, bateria, tanque):
        Motor.__init__(self, potencia)
        Eletrico.__init__(self, bateria)
        Combustao.__init__(self, tanque)

    def exibir_info(self):
        print("--- Carro Híbrido ---")
        Motor.exibir_info(self)      # Info do motor
        Eletrico.exibir_info(self)   # Info da bateria
        Combustao.exibir_info(self)  # Info do tanque


# --- Testando ---

ce = CarroEletrico(150, 75)
ce.exibir_info()    # Exibe potência e bateria
ce.ligar_motor()    # Herdado de Motor
ce.carregar()       # Herdado de Eletrico

print()

ch = CarroHibrido(200, 20, 50)
ch.exibir_info()    # Exibe potência, bateria e tanque
ch.ligar_motor()    # Herdado de Motor
ch.carregar()       # Herdado de Eletrico
ch.abastecer()      # Herdado de Combustao
