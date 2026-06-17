produto = "Notebook"
quantidade = 3
preco = 3500.00

arquivo = open("vendas.txt", "w")

arquivo.write(
    f"Venda de {quantidade} unidades de {produto} por R$ {preco:.2f} cada."
)

arquivo.close()