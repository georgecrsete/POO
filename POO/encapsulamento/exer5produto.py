# Classe que representa um produto
class Produto:
    
    # construtor da classe
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome                      # atributo privado nome
        self.__preco = preco                    # atributo privado preço
        self.__quantidade_em_estoque = quantidade_estoque  # atributo privado estoque

    # getter do nome (não tem setter porque o nome não deve mudar)
    def get_nome(self):
        return self.__nome

    # getter do preço
    def get_preco(self):
        return self.__preco

    # setter do preço com validação
    def set_preco(self, valor):
        
        # verifica se o preço é válido
        if valor >= 0:
            self.__preco = valor
        
        # impede preço negativo
        else:
            print("Preço inválido")

    # getter da quantidade em estoque
    def get_quantidade_em_estoque(self):
        return self.__quantidade_em_estoque

    # setter da quantidade com validação
    def set_quantidade_em_estoque(self, valor):
        
        # verifica se o valor é válido
        if valor >= 0:
            self.__quantidade_em_estoque = valor
        
        # impede estoque negativo
        else:
            print("Estoque inválido")

    # método para vender produtos
    def vender(self, quantidade):
        
        # verifica quantidade inválida
        if quantidade <= 0:
            print("Quantidade inválida")
        
        # verifica se tem estoque suficiente
        elif quantidade > self.__quantidade_em_estoque:
            print("Estoque insuficiente")
        
        # realiza a venda
        else:
            self.__quantidade_em_estoque -= quantidade

    # método para repor estoque
    def repor_estoque(self, quantidade):
        
        # verifica se a quantidade é válida
        if quantidade > 0:
            self.__quantidade_em_estoque += quantidade
        
        # quantidade inválida
        else:
            print("Quantidade inválida")


# criação do objeto produto
produto1 = Produto("Camisa do flamengo", 50.0, 100)

# mostrando informações iniciais
print("Nome:", produto1.get_nome())
print("Preço:", produto1.get_preco())
print("Estoque:", produto1.get_quantidade_em_estoque())

# venda de 10 unidades
produto1.vender(10)

# mostra estoque após venda
print("Estoque após venda:", produto1.get_quantidade_em_estoque())

# reposição de 20 unidades
produto1.repor_estoque(20)

# mostra estoque atualizado
print("Estoque após reposição:", produto1.get_quantidade_em_estoque())

# alteração de preço
produto1.set_preco(60)

# mostra novo preço
print("Novo preço:", produto1.get_preco())