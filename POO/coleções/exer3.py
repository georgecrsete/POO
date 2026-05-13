def adicionar_contato(agenda, nome, telefone):
    agenda[nome] = telefone
    print(f"Contato '{nome}' salvo com sucesso.")

def buscar_telefone(agenda, nome):
    if nome in agenda:
        print(f"Telefone de {nome}: {agenda[nome]}")
    else:
        print(f"Contato '{nome}' não encontrado.")

def remover_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        print(f"Contato '{nome}' removido.")
    else:
        print(f"Contato '{nome}' não existe na agenda.")

def listar_contatos(agenda):
    if not agenda:
        print("A agenda está vazia.")
        return
    print("\n--- Contatos ---")
    for nome, tel in sorted(agenda.items()):
        print(f"  {nome:20} {tel}")


agenda = {}

while True:
    print("\n[1] Adicionar  [2] Buscar  [3] Remover  [4] Listar  [5] Sair")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        n = input("Nome: ")
        t = input("Telefone: ")
        adicionar_contato(agenda, n, t)
    elif opcao == "2":
        buscar_telefone(agenda, input("Nome: "))
    elif opcao == "3":
        remover_contato(agenda, input("Nome: "))
    elif opcao == "4":
        listar_contatos(agenda)
    elif opcao == "5":
        print("Até logo!")
        break
    else:
        print("Opção inválida.")