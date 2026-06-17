arquivo = open("serialização/texto.txt", "r")

linhas = arquivo.readlines()

print("Quantidade de linhas:", len(linhas))

arquivo.close()