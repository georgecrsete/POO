# ============================================================
# EXERCÍCIO 5 - Herança + super() + Polimorfismo com lista
# Conceito: Classes filhas estendem o método da classe pai usando super(),
#           e objetos de tipos diferentes são tratados de forma uniforme
# ============================================================

# Classe PAI — funcionário genérico
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.salario:.2f}")  # :.2f = 2 casas decimais


# Classe FILHA 1 — Gerente herda de Funcionario e adiciona bônus
class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)  # Reaproveita o construtor do pai
        self.bonus = bonus

    def exibir_dados(self):
        super().exibir_dados()  # Chama o exibir_dados do pai primeiro
        print(f"Bônus: R$ {self.bonus:.2f}")  # Depois adiciona o bônus


# Classe FILHA 2 — Desenvolvedor herda de Funcionario e adiciona linguagem
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def exibir_dados(self):
        super().exibir_dados()          # Exibe dados comuns do funcionário
        print(f"Linguagem: {self.linguagem}")  # Adiciona info específica


# --- Testando as classes ---

gerente = Gerente("Leandro", 8500.00, 2000.00)
desenvolvedor = Desenvolvedor("Leo", 6000.00, "Python")

# Polimorfismo: objetos de tipos diferentes são tratados igualmente no loop
funcionarios = [gerente, desenvolvedor]

for funcionario in funcionarios:
    print(f"--- {funcionario.nome} ---")
    funcionario.exibir_dados()  # Cada um chama seu próprio exibir_dados()
    print()
