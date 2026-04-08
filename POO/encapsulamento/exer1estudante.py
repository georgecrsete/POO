# Criação da classe Estudante
class Estudante:
    
    # Método construtor (executa quando o objeto é criado)
    def __init__(self, id, nome, creditos):
        self.__id = id          # atributo privado (não deve ser acessado diretamente fora da classe)
        self.nome = nome        # atributo público (pode ser acessado diretamente)
        self.__creditos = creditos   # atributo privado


    # Método para retornar o id do estudante
    # (o ideal seria usar @property, mas assim também funciona)
    def id(self):
        return self.__id
   
    # Método para adicionar créditos ao estudante
    def adicionar_creditos(self, creditos):
        
        # verifica se o valor é positivo
        if creditos > 0:
            self.__creditos += creditos   # soma os créditos atuais com o valor informado
        
        # se for negativo ou zero
        else:
            self.__creditos = 1  
            


    # Método para mostrar os dados do estudante
    def detalhar(self):
        print("ID:", self.__id)          # mostra o id
        print("Nome:", self.nome)        # mostra o nome
        print("Créditos:", self.__creditos)   # mostra os créditos


# criação dos objetos (instâncias da classe)
e1 = Estudante(0, "Leandro", 30)   # objeto estudante com id 0
e2 = Estudante(1, "Diogo", 25)     # objeto estudante com id 1


# chamada do método para mostrar os dados
e1.detalhar()
e2.detalhar()