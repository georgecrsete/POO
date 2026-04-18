# ============================================================
# EXERCÍCIO 6 - Herança Múltipla
# Conceito: Uma classe pode herdar de DUAS ou mais classes ao mesmo tempo,
#           combinando os comportamentos de cada uma
# ============================================================

# Classe 1 — especialidade de nadar
class Nadador:
    def mover(self):
        print("Nadando...")


# Classe 2 — especialidade de correr
class Corredor:
    def mover(self):
        print("Correndo...")


# Classe com HERANÇA MÚLTIPLA — herda de Nadador E de Corredor
class Triatleta(Nadador, Corredor):
    def mover(self):
        # Como ambos os pais têm mover(), chamamos cada um explicitamente
        Nadador.mover(self)   # Chama o mover() de Nadador
        Corredor.mover(self)  # Chama o mover() de Corredor
        print("Eu sou Triatleta")  # Comportamento exclusivo


# --- Testando ---

t1 = Triatleta()
t1.mover()
# Saída:
# Nadando...
# Correndo...
# Eu sou Triatleta
