class Veiculo:
    def mover(self):
        return "veiculo se move"
    
class Carro(Veiculo):
    def mover(self):
        return "carro acelera"
    
class Moto(Veiculo):
    def mover(self):
        return "moto empina"
    
class Bicicleta(Veiculo):
    def mover(self):
        return "bicicleta pedala"
    
veiculos = [Carro(), Moto(), Bicicleta()]

for veiculo in veiculos:
    print(f"{veiculo.__class__.__name__} = {veiculo.mover()}")