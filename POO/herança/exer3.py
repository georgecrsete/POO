# ============================================================
# EXERCÍCIO 3 - Polimorfismo (mesmo método, comportamentos diferentes)
# Conceito: Duas classes com o método de mesmo nome (fazer_som),
#           mas cada uma executa de forma diferente
#
# ATENÇÃO: Neste exercício, Cachorro NÃO herda de Animal.
#          O polimorfismo aqui é chamado de "duck typing" —
#          o Python não exige herança para isso funcionar.
# ============================================================

# Classe base Animal com comportamento genérico
class Animal:
    def fazer_som(self):
        print("Um Som Desconhecido")


# Cachorro tem o mesmo método, mas com comportamento específico
# Nota: para seguir herança correta, poderia ser: class Cachorro(Animal)
class Cachorro:
    def fazer_som(self):
        print("Latido")  # Sobrescreve o comportamento padrão


# --- Testando as classes ---

animal1 = Animal()
animal1.fazer_som()   # Saída: Um Som Desconhecido

cachorro1 = Cachorro()
cachorro1.fazer_som()  # Saída: Latido
