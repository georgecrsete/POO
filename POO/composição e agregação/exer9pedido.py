# COMPOSIÇÃO: Pedido É COMPOSTO de ItemPedido (itens criados dentro do Pedido)

class ItemPedido:
    def __init__(self, produto, quantidade, preco):
        self.__produto = produto        # atributo privado
        self.__quantidade = quantidade  # atributo privado
        self.__preco = preco            # atributo privado

    def get_produto(self):              # getter → acessa __produto
        return self.__produto
    def get_quantidade(self):           # getter → acessa __quantidade
        return self.__quantidade
    def get_preco(self):                # getter → acessa __preco
        return self.__preco


class Pedido:
    def __init__(self):
        self.__lista_itens = []  # lista vazia, receberá os itens

    def adicionar_item(self, produto, quantidade, preco):
        item = ItemPedido(produto, quantidade, preco)  # COMPOSIÇÃO: item criado dentro do Pedido
        self.__lista_itens.append(item)

    def calcular_total(self):
        total = 0
        for item in self.__lista_itens:
            total += item.get_quantidade() * item.get_preco()  # quantidade × preço de cada item
        return total


pedido = Pedido()

pedido.adicionar_item("treloso",      2,  5)   # 2 × 5  = 10
pedido.adicionar_item("coca cola It", 1, 12)   # 1 × 12 = 12
pedido.adicionar_item("brigadeiro",   1,  3)   # 1 × 3  =  3

print("Total do pedido:", pedido.calcular_total())  # Total = 25S