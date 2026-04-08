class ContaBancaria:
    
    # construtor da classe
    def __init__(self, titular, saldo = 0):
        self.titular = titular     # atributo público
        self.__saldo = saldo       # atributo privado (encapsulamento)
    
    # método para retornar o saldo
    def saldo(self):
        return self.__saldo

    # método para depositar dinheiro
    def depositar(self, valor):
        
        # verifica se o valor é válido
        if valor > 0:
            self.__saldo += valor   # adiciona ao saldo
        
        # se for inválido
        else:
            print("valor menor que zero.")

    # método para sacar dinheiro
    def sacar(self, valor):
        
        # verifica se tem saldo suficiente
        if valor <= self.__saldo:
            self.__saldo -= valor   # remove do saldo
        
        # se não tiver saldo suficiente
        else:
            print("saldo insuficiente.")

    # método para mostrar as informações
    def consultar_saldo(self):
        print("Nome do titular:", self.titular)
        print("Saldo atual:", self.__saldo)


# criação do objeto
conta1 = ContaBancaria("joaozinho")

# operações
conta1.depositar(150)
conta1.sacar(100)

# mostrar dados
conta1.consultar_saldo()