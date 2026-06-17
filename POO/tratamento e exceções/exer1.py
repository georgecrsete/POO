def adicionar_valor(inicial, adicional):
    if adicional <= 0:
        raise Exception("Somente valores positivos...")
    return inicial + adicional


try:
    resultado = adicionar_valor(10, 10)
    print(resultado)  
except Exception as e:
    print(e)

try:
    resultado = adicionar_valor(10, -3)
    print(resultado)
except Exception as e:
    print(e) 
    

