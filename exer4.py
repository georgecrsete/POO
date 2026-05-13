try:
    print("abrindo arquivo...")
    e = 1/0
except ZeroDivisionError as e:
    print("deu erro")

finally:
    print("programa encerrando")
    


