# Classe Jogador
class Jogador:
    
    # construtor
    def __init__(self, nome, posicao):
        self.nome = nome        # nome do jogador
        self.posicao = posicao  # posição do jogador


# Classe Time
class Time:
    
    # construtor
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []   # lista onde serão armazenados os objetos Jogador

    # método para adicionar jogador ao time
    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)  # adiciona o objeto na lista

    # método para listar jogadores
    def listar_jogadores(self):
        print(f"Jogadores do time {self.nome}:")
        
        # percorre a lista de jogadores
        for jogador in self.jogadores:
            
            # mostra nome e posição de cada jogador
            print(jogador.nome, "-", jogador.posicao)


# Criando jogadores (objetos independentes)
j1 = Jogador("Negueba", "Atacante")
j2 = Jogador("Josenildo", "Volante")
j3 = Jogador("Walter", "Goleiro")

# Criando time
time1 = Time("Mirassol")

# Adicionando jogadores ao time
time1.adicionar_jogador(j1)
time1.adicionar_jogador(j2)
time1.adicionar_jogador(j3)

# Listar jogadores
time1.listar_jogadores()