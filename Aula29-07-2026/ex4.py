class Conta:
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.numero = None
        self.saldo = 0
 
    def inserirDados(self, nome, cpf, numero, saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo
 
    def depositar(self, valor):
        self.saldo += valor
        print("Depósito realizado! Novo saldo:", self.saldo)
 
    def sacar(self, valor):
        if self.saldo > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print("Saque realizado! Novo saldo:", self.saldo)
            else:
                print("Saldo insuficiente para esse saque!")
        else:
            print("Conta sem saldo, não é possível sacar!")
 
    def imprimir_saldo(self):
        print("Saldo atual:", self.saldo)
 
 
conta = Conta()
nome = input("Insira o nome do cliente: ")
cpf = input("Insira o CPF do cliente: ")
numero = input("Insira o número da conta: ")
saldo = float(input("Insira o saldo inicial da conta: "))
conta.inserirDados(nome, cpf, numero, saldo)
 
operacao = input("Deseja depositar ou sacar (D/S)?: ")
valor = float(input("Insira o valor da operação: "))
if operacao.lower() == "d":
    conta.depositar(valor)
elif operacao.lower() == "s":
    conta.sacar(valor)
conta.imprimir_saldo()