# ============================================================
# EXERCÍCIO 2 - Herança com Valor Padrão no Construtor
# Conceito: A classe filha pode definir valores padrão nos parâmetros,
#           tornando a criação de objetos mais prática
# ============================================================

# Classe PAI — representa qualquer Animal
class Animal:
    def __init__(self, grupo):
        self.grupo: str = grupo  # Ex: "Herbívoros", "Mamíferos"

    def __str__(self):
        return f"O Animal é do grupo: {self.grupo}"


# Classe FILHA — herda de Animal
# O parâmetro 'grupo' já tem valor padrão "Mamíferos"
# Isso significa que podemos criar um Cachorro sem passar nenhum argumento
class Cachorro(Animal):
    def __init__(self, grupo="Mamíferos"):
        # Repassa o grupo (padrão ou informado) para o construtor da classe pai
        super().__init__(grupo)


# --- Testando as classes ---

animal1 = Animal("Herbívoros")  # Precisa informar o grupo
print(animal1)

cao1 = Cachorro()  # Não precisa informar nada — usa o padrão "Mamíferos"
print(cao1)  # Usa o __str__ herdado de Animal
