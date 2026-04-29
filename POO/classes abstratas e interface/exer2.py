from abc import ABC, abstractmethod

class DispositivoEletronico(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass

class Carregavel(ABC):
    @abstractmethod
    def carregar(self):
        pass

class Smartfone( DispositivoEletronico, Carregavel):
    def ligar(self):
        print("celular ligando")

    def desligar(self):
        print("celular desligando")

    def carregar(self):
        print("celular carregando")
    
class Notebook(DispositivoEletronico, Carregavel):
    def ligar(self):
        print("pc ligando")

    def desligar(self):
        print("pc desligando")

    def carregar(self):
        print("pc carregando")


class FoneOuvido(DispositivoEletronico):
    def ligar(self):
        print("fone ligando")

    def desligar(self):
        print("fone desligando")

dispositivos = [Smartfone(), Notebook(), FoneOuvido()]
for dispositivo in dispositivos:
    print(f'{dispositivo.__class__.__name__}:')
    dispositivo.ligar()
    dispositivo.desligar()
    print("-------------------")

carregadores = [Smartfone(), Notebook()]
for bateria in carregadores:
    print(f'{bateria.__class__.__name__}:') 
    bateria.carregar()
    print("-------------------")
