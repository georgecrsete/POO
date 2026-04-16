class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.salario:.2f}")


class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Bônus: R$ {self.bonus:.2f}")


class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Linguagem: {self.linguagem}")



gerente = Gerente("Leandro", 8500.00, 2000.00)
desenvolvedor = Desenvolvedor("Leo", 6000.00, "Python")


funcionarios = [gerente, desenvolvedor]

for funcionario in funcionarios:
    print(f"--- {funcionario.nome} ---")
    funcionario.exibir_dados()
    print()