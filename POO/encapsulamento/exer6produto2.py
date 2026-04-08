# Classe que representa um produto
class Produto:
    
    # construtor
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome   # atributo privado (nome não deve ser alterado diretamente)
        
        # usa os setters automaticamente (boa prática)
        self.preco = preco
        self.quantidade_em_estoque = quantidade_estoque

    # getter do nome (sem setter porque normalmente o nome não muda)
    def get_nome(self):
        return self.__nome

    # property do preço (getter)
    @property
    def preco(self):
        return self.__preco

    # setter do preço com validação
    @preco.setter
    def preco(self, valor):
        
        # impede preço negativo
        if valor >= 0:
            self.__preco = valor
        else:
            print("Preço não pode ser negativo")

    # property do estoque (getter)
    @property
    def quantidade_em_estoque(self):
        return self.__quantidade_em_estoque

    # setter do estoque com validação
    @quantidade_em_estoque.setter
    def quantidade_em_estoque(self, valor):
        
        # impede estoque negativo
        if valor >= 0:
            self.__quantidade_em_estoque = valor
        else:
            print("Quantidade não pode ser negativa")

    # método para vender produtos
    def vender(self, quantidade):
        
        # verifica quantidade inválida
        if quantidade <= 0:
            print("Quantidade inválida")
        
        # verifica estoque suficiente
        elif quantidade > self.__quantidade_em_estoque:
            print("Estoque insuficiente")
        
        # realiza a venda
        else:
            self.__quantidade_em_estoque -= quantidade

    # método para repor estoque
    def repor_estoque(self, quantidade):
        
        # verifica quantidade válida
        if quantidade > 0:
            self.__quantidade_em_estoque += quantidade
        
        # quantidade inválida
        else:
            print("Quantidade inválida")


# criação do produto
produto1 = Produto("Camisa do flamengo", 50.0, 100)

# mostrando dados
print("Nome:", produto1.get_nome())

# acessando property (sem parênteses)
print("Preço:", produto1.preco)
print("Estoque:", produto1.quantidade_em_estoque)

# venda
produto1.vender(10)
print("Estoque após venda:", produto1.quantidade_em_estoque)

# reposição
produto1.repor_estoque(20)
print("Estoque após reposição:", produto1.quantidade_em_estoque)

# alteração do preço usando setter automaticamente
produto1.preco = 70
print("Novo preço:", produto1.preco)