class Animal:
    def __init__(self,grupo):
        self.grupo:str = grupo
    def __str__(self):
        return f"O Animal é do grupo: {self.grupo}"
class Cachorro(Animal):
    def __init__(self, grupo = "Mamíferos"):
        super().__init__(grupo)


animal1 = Animal("Herbívoros")
print(animal1)
cao1 = Cachorro()
print(cao1)