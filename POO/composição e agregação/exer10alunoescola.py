# COMPOSIÇÃO + AGREGAÇÃO juntas:
# Escola cria as Turmas (Composição)
# Turma recebe Alunos já criados fora (Agregação)

class Escola:
    def __init__(self, nome):
        self.__nome = nome
        self.__lista_turmas = []  # lista vazia de turmas

    def adicionar_turma(self, nome):
        turma = Turma(nome)               # COMPOSIÇÃO: Turma criada dentro da Escola
        self.__lista_turmas.append(turma)
        return turma                      # retorna a turma para poder adicionar alunos nela

    def listar_turmas(self):
        for turma in self.__lista_turmas:
            print("Turma:", turma.get_nome())
            for aluno in turma.get_alunos():  # percorre os alunos de cada turma
                print("  Aluno:", aluno.get_nome())


class Turma:
    def __init__(self, nome):
        self.__nome = nome
        self.__lista_alunos = []  # lista vazia de alunos

    def adicionar_aluno(self, aluno):
        self.__lista_alunos.append(aluno)  # AGREGAÇÃO: recebe Aluno já criado fora

    def get_nome(self):
        return self.__nome

    def get_alunos(self):
        return self.__lista_alunos  # retorna a lista para o listar_turmas() da Escola


class Aluno:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):       # getter → acessa __nome
        return self.__nome


escola = Escola("IFRN")

turma1 = escola.adicionar_turma("info2v")  # Turma criada dentro da Escola (Composição)

aluno1 = Aluno("leandro")  # Alunos criados FORA da Turma (Agregação)
aluno2 = Aluno("leo")

turma1.adicionar_aluno(aluno1)  # alunos passados como parâmetro
turma1.adicionar_aluno(aluno2)

escola.listar_turmas()

