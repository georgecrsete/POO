import string

frase = input("Digite uma frase: ")


frase = frase.lower()
for p in string.punctuation:
    frase = frase.replace(p, "")

palavras = frase.split()


unicas = set(palavras)


frequencia = {}
for p in palavras:
    frequencia[p] = frequencia.get(p, 0) + 1


print("\n--- Palavras únicas ---")
print(", ".join(sorted(unicas)))

print("\n--- Frequência (ordem alfabética) ---")
for palavra, qtd in sorted(frequencia.items()):
    print(f"  {palavra:15} → {qtd}")