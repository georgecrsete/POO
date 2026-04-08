# AGREGAÇÃO: Biblioteca USA Livros criados fora dela
# (diferente de Composição, onde os objetos seriam criados dentro)

class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo  # atributo privado
        self.__autor = autor    # atributo privado

    def get_titulo(self):       # getter → acessa __titulo
        return self.__titulo
    
    def get_autor(self):        # getter → acessa __autor
        return self.__autor


class Biblioteca:
    def __init__(self, nome):
        self.__nome = nome
        self.__lista_livros = []  # lista vazia, receberá os livros

    def adicionar_livro(self, livro):
        self.__lista_livros.append(livro)  # recebe objeto Livro já criado

    def listar_livros(self):
        for livro in self.__lista_livros:  # percorre a lista
            print("Titulo:", livro.get_titulo(),
                  "Autor:",  livro.get_autor())


# AGREGAÇÃO: Livros criados FORA da Biblioteca
# eles existem independente dela
livro1 = Livro("diario de um banana", "banana")
livro2 = Livro("o ultimo homem", "homem")

biblioteca = Biblioteca("Biblioteca Central")

biblioteca.adicionar_livro(livro1)  # livro passado como parâmetro
biblioteca.adicionar_livro(livro2)

biblioteca.listar_livros()

# Saída:
# Titulo: diario de um banana Autor: banana
# Titulo: o ultimo homem Autor: homem