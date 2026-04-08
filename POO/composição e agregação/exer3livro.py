# Classe Autor
class Autor:
    
    # construtor
    def __init__(self, nome):
        self.nome = nome   # nome do autor


# Classe Livro
class Livro:
    
    # construtor
    def __init__(self, nome_autor):
        
        # aqui acontece COMPOSIÇÃO
        # o livro cria o objeto Autor internamente
        self.autor = Autor(nome_autor)


# criação do livro (que automaticamente cria o autor)
livro1 = Livro("George")

# acessando o nome do autor através do livro
print("Nome do autor:", livro1.autor.nome)