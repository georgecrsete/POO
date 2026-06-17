import tkinter as tk
from tkinter import messagebox, simpledialog

class ContaBancaria:
    numeros_contas = []

    def __init__(self, titular, numero, saldo):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
        ContaBancaria.numeros_contas.append(numero)

    def get_saldo(self):
        return self.__saldo

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor  # era self.saldo (sem __)
            return True
        return False

    def sacar(self, valor):
        if self.__saldo >= valor and valor > 0:  # era > sem =
            self.__saldo -= valor
            return True
        return False

    def exibir_dados(self):
        return f"{self.__titular}, Número da conta: {self.__numero}, Saldo: R$ {self.__saldo:.2f}"  # era print, mas precisa retornar

    @classmethod
    def existe_conta_duplicada(cls):
        return len(cls.numeros_contas) != len(set(cls.numeros_contas))

    @classmethod  
    def contas_duplicadas(cls):
        vistas = []
        duplicadas = []
        for numero in cls.numeros_contas:
            if numero in vistas:
                duplicadas.append(numero)
            else:
                vistas.append(numero)
        return duplicadas  


class BancoApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema Bancário - POO em Python")
        self.janela.geometry("850x400")

        self.contas = [
            ContaBancaria("João", 1001, 500),
            ContaBancaria("Maria", 1001, 1000),
            ContaBancaria("Pedro", 1003, 300),
            ContaBancaria("Esther", 1004, 20)
        ]

        if ContaBancaria.existe_conta_duplicada():
            messagebox.showerror("Erro", "Existe conta duplicada")
            messagebox.showinfo("Contas duplicadas", str(ContaBancaria.contas_duplicadas()))
            exit()

        self.criar_interface()

    def criar_interface(self):
        titulo = tk.Label(
            self.janela,
            text="Banco Python - Contas Bancárias",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        self.frame_numeros = tk.Frame(self.janela)
        self.frame_numeros.pack()

        self.atualizar_tela()

    def atualizar_tela(self):
        for widget in self.frame_numeros.winfo_children():
            widget.destroy()

        for conta in self.contas:  # era self.numeros (atributo inexistente)
            frame = tk.Frame(
                self.frame_numeros,
                borderwidth=2,
                relief="groove",
                padx=10,
                pady=10
            )
            frame.pack(side="left", padx=10, pady=10)

            tk.Label(frame, text=conta.get_titular(), font=("Arial", 14, "bold")).pack()
            tk.Label(frame, text=f"Número: {conta.get_numero()}").pack()
            tk.Label(frame, text=f"Saldo: R$ {conta.get_saldo():.2f}", font=("Arial", 12)).pack(pady=5)

            tk.Button(frame, text="Depositar", width=15, command=lambda c=conta: self.depositar(c)).pack(pady=2)
            tk.Button(frame, text="Sacar", width=15, command=lambda c=conta: self.sacar(c)).pack(pady=2)
            tk.Button(frame, text="Transferir", width=15, command=lambda c=conta: self.transferir(c)).pack(pady=2)
            tk.Button(frame, text="Exibir Dados", width=15, command=lambda c=conta: self.exibir_dados(c)).pack(pady=2)

    def depositar(self, conta):
        valor = simpledialog.askfloat("Depósito", "Digite o valor do depósito:")
        if valor is not None:
            if conta.depositar(valor):
                messagebox.showinfo("Sucesso", "Depósito realizado.")
            else:
                messagebox.showerror("Erro", "Valor inválido.")
        self.atualizar_tela()

    def sacar(self, conta):
        valor = simpledialog.askfloat("Saque", "Digite o valor do saque:")
        if valor is not None:
            if conta.sacar(valor):
                messagebox.showinfo("Sucesso", "Saque realizado.")
            else:
                messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido.")
        self.atualizar_tela()

    def transferir(self, conta_origem):
        valor = simpledialog.askfloat("Transferência", "Digite o valor:")
        if valor is None:
            return

        numero_destino = simpledialog.askinteger("Transferência", "Digite o número da conta destino:")

        conta_destino = None
        for conta in self.contas:  # era self.numeros
            if conta.get_numero() == numero_destino:
                conta_destino = conta
                break

        if conta_destino is None:
            messagebox.showerror("Erro", "Conta destino não encontrada.")
            return

        if conta_origem == conta_destino:
            messagebox.showerror("Erro", "Não é possível transferir para a mesma conta.")
            return

        if conta_origem.sacar(valor):  # transferir não existe, usa sacar + depositar
            conta_destino.depositar(valor)
            messagebox.showinfo("Sucesso", "Transferência realizada.")
        else:
            messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido.")

        self.atualizar_tela()

    def exibir_dados(self, conta):
        messagebox.showinfo("Dados da Conta", conta.exibir_dados())  # exibir_dados agora retorna string


janela = tk.Tk()
app = BancoApp(janela)
janela.mainloop()