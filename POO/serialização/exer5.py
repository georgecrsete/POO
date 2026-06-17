def registrar_log(mensagem):
    arquivo = open("sistema.log", "a")
    arquivo.write(mensagem + "\n")
    arquivo.close()

registrar_log("Usuário entrou no sistema")
registrar_log("Arquivo criado")
registrar_log("Sistema encerrado")