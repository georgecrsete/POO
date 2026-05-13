contagem = {}  

print("Digite os anos de nascimento (Enter vazio para encerrar):")

while True:
    entrada = input("Ano: ").strip()

    if entrada == "":
        break

    if not entrada.isdigit():
        print("Entrada inválida. Digite apenas números.")
        continue

    ano = int(entrada)
    contagem[ano] = contagem.get(ano, 0) + 1


print("\n--- Relatório ---")
for ano in sorted(contagem):
    print(f"{ano}: {contagem[ano]} pessoas")