class Animal():
    def emitir_som(self):
        return "barulho"
    
class Cachorro(Animal):
    def emitir_som(self):
        return "au au"
    
class Gato(Animal):
    def emitir_som(self):
        return "miau miau"

animais = [Animal(), Cachorro(), Gato()]

for animal in animais:
    print(f"O {animal.__class__.__name__} = {animal.emitir_som()}")