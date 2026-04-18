# ============================================================
# EXERCÍCIO 7 - Polimorfismo com Herança
# Conceito: Cada classe filha sobrescreve o método da classe pai
#           para ter seu próprio comportamento específico
# ============================================================

# Classe PAI — comportamento genérico de qualquer veículo
class Veiculo:
    def acelerar(self):
        print("Acelerando")


# Classe FILHA 1 — sobrescreve acelerar() com mensagem específica
class Moto(Veiculo):
    def acelerar(self):
        print("Acelerando minha Moto")  # Comportamento próprio da Moto


# Classe FILHA 2 — também sobrescreve acelerar()
class Carro(Veiculo):
    def acelerar(self):
        print("Acelerando meu Carro")  # Comportamento próprio do Carro


# --- Testando ---

veiculo1 = Veiculo()
veiculo1.acelerar()  # Saída: Acelerando

moto1 = Moto()
moto1.acelerar()     # Saída: Acelerando minha Moto

carro1 = Carro()
carro1.acelerar()    # Saída: Acelerando meu Carro
