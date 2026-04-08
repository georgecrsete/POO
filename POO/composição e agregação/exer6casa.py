# Classe Comodo
class Comodo:
    
    # construtor
    def __init__(self, nome, tamanho):
        self.__nome = nome        # atributo privado nome do cômodo
        self.__tamanho = tamanho  # atributo privado tamanho

    # getter do nome
    def get_nome(self):
        return self.__nome

    # getter do tamanho
    def get_tamanho(self):
        return self.__tamanho


# Classe Casa
class Casa:
    
    # construtor recebe uma lista de cômodos
    def __init__(self, lista_comodos):
        self.__lista_comodos = lista_comodos   # lista de objetos Comodo

    # método para criar e adicionar um cômodo (COMPOSIÇÃO)
    def adicionar_comodo(self, nome, tamanho):
        
        # cria o objeto dentro da casa
        comodo = Comodo(nome, tamanho)  
        
        # adiciona na lista
        self.__lista_comodos.append(comodo)
    
    # método para listar os cômodos
    def listar_comodos(self):
        
        # percorre a lista
        for comodo in self.__lista_comodos:
            
            # mostra os dados de cada cômodo
            print(f"Comodo: {comodo.get_nome()}, Tamanho do comodo: {comodo.get_tamanho()}m")


# criação da casa (lista vazia)
casa = Casa([])

# adicionando cômodos
casa.adicionar_comodo("banheiro", 10)
casa.adicionar_comodo("Cozinha", 15)    

# listando cômodos
casa.listar_comodos()