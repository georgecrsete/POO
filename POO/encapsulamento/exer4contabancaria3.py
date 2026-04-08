# Classe que representa uma conta bancária
class ContaBancaria:
    
    # construtor da classe
    def __init__(self, saldo_inicial=0):
        # atributo privado (encapsulamento)
        self.__saldo = saldo_inicial

    # getter usando @property (permite acessar como atributo)
    @property
    def saldo(self):
        return self.__saldo   # retorna o saldo atual
   
    # setter usando @property (permite modificar com validação)
    @saldo.setter
    def saldo(self, valor):
        
        # verifica se o valor é válido
        if valor >= 0:
            self.__saldo = valor
        
        # impede saldo negativo
        else:
            print("Saldo não pode ser negativo")

    # método para depositar dinheiro
    def depositar(self, valor):
        
        # verifica se o valor é positivo
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado.")
        
        # se for inválido
        else:
            print("Valor de depósito inválido.")

    # método para sacar dinheiro
    def sacar(self, valor):
        
        # verifica se o valor é válido
        if valor <= 0:
            print("Valor de saque inválido.")
        
        # verifica se tem saldo suficiente
        elif valor > self.__saldo:
            print("Saldo insuficiente.")
        
        # realiza o saque
        else:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado.")


# criação da conta com saldo inicial
conta = ContaBancaria(50)

# depósito
conta.depositar(50)

# saques
conta.sacar(30)
conta.sacar(3)

# acessando o saldo usando property (sem parênteses)
print("Meu saldo:", conta.saldo)