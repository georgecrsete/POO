class Veiculo:
     def acelerar(self): 
          print("Acelerando")
class Moto(Veiculo):
     def acelerar(self): 
          print("Acelerando minha Moto")
class Carro(Veiculo):
     def acelerar(self): 
          print("Acelerando meu Carro")

veiculo1 = Veiculo()
veiculo1.acelerar()
moto1 = Moto()
moto1.acelerar()
carro1 = Carro()
carro1.acelerar()