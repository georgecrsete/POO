# COMPOSIÇÃO: Computador É COMPOSTO de Processador e Memória

class Processador:
    def __init__(self, modelo, velocidade):
        self.__modelo = modelo        # atributo privado
        self.__velocidade = velocidade

    def get_modelo(self):             # getter → acessa __modelo
        return self.__modelo
    
    def get_velocidade(self):         # getter → acessa __velocidade
        return self.__velocidade


class Memoria:
    def __init__(self, capacidade):
        self.__capacidade = capacidade  # atributo privado

    def get_capacidade(self):           # getter → acessa __capacidade
        return self.__capacidade


class Computador:
    def __init__(self, modelo, velocidade, capacidade):
        # COMPOSIÇÃO: objetos criados dentro do Computador
        self.__processador = Processador(modelo, velocidade)  # parte 1
        self.__memoria = Memoria(capacidade)                  # parte 2

    def exibir_configuracao(self):
        # acessa os dados via getters (atributos são privados)
        print("Processador:", self.__processador.get_modelo())
        print("Velocidade:",  self.__processador.get_velocidade())
        print("Memória:",     self.__memoria.get_capacidade())


# cria o computador passando os dados de uma vez
computador = Computador("Intel Core i7", "3.6 GHz", "16 GB")
computador.exibir_configuracao()

# Saída:
# Processador: Intel Core i7
# Velocidade:  3.6 GHz
# Memória:     16 GB