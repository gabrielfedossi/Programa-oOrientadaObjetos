class Pessoa:
    def __init__(self):
        self.nome = None
        self.idade = 0
        self.endereco = None

    def inserirDados(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def alterarIdade(self, idade):
        self.idade = idade

    def imprimir(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Endereço:", self.endereco)

pessoa = Pessoa()

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
endereco = input("Insira seu endereço: ")
alterar = input("Deseja alterar idade (S/N)?: ")

pessoa.inserirDados(nome, idade, endereco)
pessoa.imprimir()
if alterar.lower() == "s":
    idade = int(input("Insira sua idade: "))
    pessoa.alterarIdade(idade)
pessoa.imprimir()


        