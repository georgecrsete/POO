import tkinter as tk
from tkinter import messagebox, simpledialog
from bancoapp import Cliente, ContaBancaria, Endereco


class ContaCorrente(ContaBancaria):
    def __init__(self, cliente, numero, saldo, limite, tarifa_mensal):
        super().__init__(cliente, numero, saldo)
        self.__limite = limite
        self.__tarifa_mensal = tarifa_mensal

    def cobrar_tarifa(self):
        super().sacar(self.__tarifa_mensal)

    def sacar(self, valor):
        saldo_total = self.get_saldo() + self.__limite

        if valor <= saldo_total:
            return super().sacar(valor)
        return False

    def exibir_dados(self):
        return (
            super().exibir_dados() +
            f"\nTipo: {self.get_tipo_conta()}"
            f"\nlimite: {self.__limite}" +
            f"\ntarifa: {self.__tarifa_mensal}"
        )
    def get_tipo_conta(self):
        return "Conta Corrente"

class ContaPoupanca(ContaBancaria):
    def __init__(self, cliente, numero, saldo, taxa_rendimento: float):
        super().__init__(cliente, numero, saldo)
        self.__taxa_rendimento = taxa_rendimento

    def sacar(self, valor):
        return super().sacar(valor)


    def render_juros(self):
        juros = self.get_saldo() * self.__taxa_rendimento
        self.depositar(juros)
    
    def exibir_dados(self):
        return (
            super().exibir_dados() +
            f"\nTipo: {self.get_tipo_conta()}" +
            f"\nTaxa de rendimento: {self.__taxa_rendimento}"
        )

    def get_tipo_conta(self):
        return "Conta Poupança"



class BancoApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema Bancário - POO em Python")
        self.janela.geometry("850x400")

        cliente1 = Cliente("Leo", "676.676", Endereco("Santa Terezinha", "456", "Bom Jesus", "Ceará-Mirim") )
        cliente2 = Cliente("Caio", "456.909", Endereco("Av. Brasil", "984", "Xique-xique", "São Gonçalo") )
        # cliente3 = Cliente("Sofócles", "123.456", Endereco("Avelino cruz", "67", "Baxa", "Pureza") )
        # cliente4 = Cliente("Dhimy", "900.865", Endereco("Palha", "001", "Cohab", "Brogodó") )

        self.contas = [
            ContaCorrente(cliente1, 1001, 500, 300, 15),
            ContaPoupanca(cliente2, 1002, 1000, 0.05),
            # ContaBancaria(cliente3, 1003, 300),
            # ContaBancaria(cliente4, 1004, 20)
            ]

        # messagebox.showinfo("Sucesso", "Depósito realizado.")

        self.criar_interface()

    def criar_interface(self):
        titulo = tk.Label(
            self.janela,
            text="Banco Python - Contas Bancárias",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        self.frame_contas = tk.Frame(self.janela)
        self.frame_contas.pack()

        self.atualizar_tela()

    def atualizar_tela(self):
        for widget in self.frame_contas.winfo_children():
            widget.destroy()

        for conta in self.contas:
            frame = tk.Frame(
                self.frame_contas,
                borderwidth=2,
                relief="groove",
                padx=10,
                pady=10
            )
            frame.pack(side="left", padx=10, pady=10)

            lbl_titular = tk.Label(
                frame,
                text=conta.get_titular().get_nome(),
                font=("Arial", 14, "bold")
            )
            lbl_titular.pack()

            lbl_numero = tk.Label(
                frame,
                text=f"Conta: {conta.get_numero()}"
            )
            lbl_numero.pack()

            lbl_saldo = tk.Label(
                frame,
                text=f"Saldo: R$ {conta.get_saldo():.2f}",
                font=("Arial", 12)
            )
            lbl_saldo.pack(pady=5)

            btn_depositar = tk.Button(
                frame,
                text="Depositar",
                width=15,
                command=lambda c=conta: self.depositar(c)
            )
            # btn_depositar.config(state="disabled")
            btn_depositar.pack(pady=2)

            btn_sacar = tk.Button(
                frame,
                text="Sacar",
                width=15,
                command=lambda c=conta: self.sacar(c)
            )
            # btn_sacar.config(state="disabled")
            btn_sacar.pack(pady=2)

            btn_transferir = tk.Button(
                frame,
                text="Transferir",
                width=15,
                command=lambda c=conta: self.transferir(c)
            )
            # btn_transferir.config(state="disabled")
            btn_transferir.pack(pady=2)

            btn_dados = tk.Button(
                frame,
                text="Exibir Dados",
                width=15,
                command=lambda c=conta: self.exibir_dados(c)
            )
            # btn_dados.config(state="disabled")
            btn_dados.pack(pady=2)

            btn_rendimento = tk.Button(
                frame,
                text="Render Juros",
                width=15,
                command=lambda c=conta: self.render_juros(c)
            )
            # btn_rendimento.config(state="disabled")
            btn_rendimento.pack(pady=2)

            btn_taxa = tk.Button(
                frame,
                text="Cobrar Taxa",
                width=15,
                command=lambda c=conta: self.cobrar_tarifa(c)
            )
            # btn_taxa.config(state="disabled")
            btn_taxa.pack(pady=2)

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

        numero_destino = simpledialog.askinteger(
            "Transferência",
            "Digite o número da conta destino:"
        )

        conta_destino = None

        for conta in self.contas:
            if conta.get_numero() == numero_destino:
                conta_destino = conta
                break

        if conta_destino is None:
            messagebox.showerror("Erro", "Conta destino não encontrada.")
            return

        if conta_origem == conta_destino:
            messagebox.showerror("Erro", "Não é possível transferir para a mesma conta.")
            return

        if conta_origem.transferir(valor, conta_destino):
            messagebox.showinfo("Sucesso", "Transferência realizada.")
        else:
            messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido.")

        self.atualizar_tela()

    def exibir_dados(self, conta):
        messagebox.showinfo("Dados da Conta", conta.exibir_dados())

    def render_juros(self, conta):
        if(conta.get_tipo_conta() == "Conta Poupança"):
            conta.render_juros()
            messagebox.showerror("Sucesso", "Rendimento efetuado.")
        else:
            messagebox.showerror("Erro", "Conta não disponibiliza rendimento")
    
    def cobrar_tarifa(self, conta):
        if(conta.get_tipo_conta() == "Conta Corrente"):
            conta.cobrar_tarifa()
            messagebox.showerror("Sucesso", "Rendimento efetuado.")
        else:
            messagebox.showerror("Erro", "Cobrança invalida para essa conta")



janela = tk.Tk()
app = BancoApp(janela)
janela.mainloop()