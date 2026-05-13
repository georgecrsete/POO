def verificar_nota(nota):
    if nota <= 0 or nota > 10:
        raise ValueError("Nota inválida(Tem que ser maior entre 1 ou 10)")
    return nota

try:
    resultado = verificar_nota(0)
    print(f"sua nota é {resultado}")

except ValueError as e:
    print(e)