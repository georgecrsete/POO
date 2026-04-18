# ============================================================
# EXERCÍCIO 1 - Herança Simples
# Conceito: Uma classe filha herda atributos e métodos da classe pai
# ============================================================

# Classe PAI (superclasse) — define o modelo base de um Computador
class Computador:
    def __init__(self, processador, memoria):
        # Atributos comuns a todo computador
        self.processador: str = processador
        self.memoria: int = memoria

    def __str__(self):
        # Método especial que define como o objeto é exibido com print()
        return f"O Processador dessa máquina é o {self.processador} com memória de {self.memoria} RAM"


# Classe FILHA — herda tudo de Computador e adiciona atributo próprio
class Laptop(Computador):
    def __init__(self, processador, memoria):
        # super().__init__() chama o construtor da classe pai
        # assim não precisamos repetir o código de processador e memoria
        super().__init__(processador, memoria)
        self.bateria_watts = 0  # Atributo exclusivo do Laptop


# Outra classe FILHA — também herda de Computador
class Desktop(Computador):
    def __init__(self, processador, memoria):
        super().__init__(processador, memoria)
        self.cabinete: str = ""  # Atributo exclusivo do Desktop


# --- Testando as classes ---

laptop = Laptop("Intel i5", 16)
print(laptop)  # Usa o __str__ herdado de Computador

desktop = Desktop("SSD 5i", 32)
print(desktop)  # Idem
