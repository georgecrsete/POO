# Classe Cidade
class Cidade:
    
    # construtor
    def __init__(self, nome):
        self.__nome = nome   # atributo privado

    # property para acessar o nome da cidade
    @property
    def nome(self):
        return self.__nome


# Classe Pessoa
class Pessoa:
    
    # recebe um objeto Cidade (agregação)
    def __init__(self, nome, cidade):
        self.nome = nome        # nome da pessoa
        self.cidade = cidade    # objeto Cidade associado


# Classe Animal
class Animal:
    
    # recebe um objeto Pessoa (agregação)
    def __init__(self, nome, dono):
        self.nome = nome     # nome do animal
        self.dono = dono     # objeto Pessoa (dono do animal)


# criação do objeto cidade
cidade1 = Cidade("Natal")

# criação da pessoa associada à cidade
pessoa1 = Pessoa("george", cidade1)

# criação do animal associado à pessoa
animal1 = Animal("dom", pessoa1)

# acessando os dados
print(animal1.nome)                # nome do animal
print(animal1.dono.nome)          # nome do dono
print(animal1.dono.cidade.nome)   # nome da cidade do dono