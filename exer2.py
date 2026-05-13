def divisao_segura(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Não pode dividir por 0")
    except TypeError:
        print("Tem que ser números")
    


resultado = divisao_segura(10, "")
print(resultado)