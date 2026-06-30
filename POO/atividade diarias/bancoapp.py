import tkinter as tk
from tkinter import messagebox, simpledialog

class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__contas = []
        self.__endereco = endereco

    def adicionar_contas(self, conta):
        self.__contas.append(conta)
    
    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_endereco(self):
        return self.__endereco

    
    def exibir_dados(self):
        return f"Nome: {self.get_nome()}, CPF: {self.get_cpf()}, Endereço: {self.get_endereco()}"

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

class Endereco:
    def __init__(self, rua, numero, bairro, cidade):
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade

    def get_rua(self):
        return self.__rua
    
    def get_numero(self):
        return self.__numero
    
    def get_bairro(self):
        return self.__bairro
    
    def get_cidade(self):
        return self.__cidade
    
    def exibir_dados(self):
        return f"Cidade: {self.get_cidade()},\nBairro: {self.get_bairro()},\nRua: {self.get_rua()},\nNúmero: {self.get_numero()}"


class ContaBancaria:
    numeros_contas = []

    def __init__(self, cliente, numero, saldo):
        self.__cliente = cliente
        self.__numero = numero
        self.__saldo = saldo
        ContaBancaria.numeros_contas.append(numero)

    def get_titular(self):
        return self.__cliente  

    def get_saldo(self):
        return self.__saldo

    def get_numero(self):
        return self.__numero

    def depositar(self, valor):
        if valor < 0:
            return False
        else:
            self.__saldo += valor
            return True

    def sacar(self, valor):
        if valor < 0:
            return False
        elif valor > self.__saldo:
            return False
        else:
            self.__saldo -= valor
            return True

    def transferir(self, valor, destino):
        if self.sacar(valor):
            destino.depositar(valor)
            return True
        else:
            return False

    def exibir_dados(self):
        c = self.__cliente
        end = c.get_endereco()
        return (
        f"Nome: {c.get_nome()}\n"
        f"CPF: {c.get_cpf()}\n"
        f"{end.exibir_dados()}\n"
        f"Número da conta: {self.__numero}\n"
        f"Saldo: R$ {self.__saldo:.2f}"
    )
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

       
