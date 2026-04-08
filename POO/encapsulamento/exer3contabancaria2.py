class ContaBancaria:
    
    # construtor da classe
    def __init__(self, saldo_inicial=0):
        self.__saldo = 0              # inicializa o saldo como 0 (segurança)
        self.set_saldo(saldo_inicial) # usa o setter para validar o saldo inicial

    # getter → retorna o saldo (encapsulamento)
    def get_saldo(self):
        return self.__saldo
    
    # setter → altera o saldo com validação
    def set_saldo(self, valor):
        
        # verifica se o valor é válido
        if valor >= 0:
            self.__saldo = valor
        
        # impede saldo negativo
        else:
            print("Saldo não pode ser negativo.")

    # método de depósito
    def depositar(self, valor):
        
        # valida valor positivo
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado.")
        
        # valor inválido
        else:
            print("Valor de depósito inválido.")

    # método de saque
    def sacar(self, valor):
        
        # verifica valor inválido
        if valor <= 0:
            print("Valor de saque inválido.")
        
        # verifica saldo insuficiente
        elif valor > self.__saldo:
            print("Saldo insuficiente.")
        
        # saque válido
        else:
            self.__saldo -= valor
            print(f"Saque de {valor} feito.")

    
# criação do objeto com saldo inicial
conta = ContaBancaria(50)

# depósito
conta.depositar(50)

# saques
conta.sacar(30)
conta.sacar(3)

# mostra saldo final
print("meu saldo:", conta.get_saldo())