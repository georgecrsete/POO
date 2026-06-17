arquivo = open("convidados.txt", "w")

for i in range(5):
    nome = input("Digite um nome: ")
    arquivo.write(nome + "\n")

arquivo.close()

print("Nomes salvos!")