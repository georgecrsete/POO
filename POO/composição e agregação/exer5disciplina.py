# Classe Professor
class Professor:
    
    # construtor
    def __init__(self, nome, titulacao):
        self.__nome = nome             # atributo privado nome
        self.__titulacao = titulacao   # atributo privado titulação 

    # getter do nome
    def get_nome(self):
        return self.__nome

    # getter da titulação
    def get_titulacao(self):
        return self.__titulacao   # ERRO ⚠️ (nome diferente do atributo)
    

# Classe Disciplina
class Disciplina:
    
    # recebe um professor já criado (agregação)
    def __init__(self, nome, professor):
        self.__nome = nome
        self.__professor = professor

    # método para mostrar informações
    def exibir_informacoes(self):
        print(f"Professor: {self.__professor.get_nome()}")
        print(f"Disciplina: {self.__nome}")
        

# criação do professor
prof1 = Professor("prof. robson", "mestrado")

# criação da disciplina associando o professor
disciplina1 = Disciplina("Educação fisica", prof1)

# mostra as informações
disciplina1.exibir_informacoes()