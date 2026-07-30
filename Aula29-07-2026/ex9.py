class AlunoAcademia:
    def __init__(self):
        self.nome = None
        self.idade = 0
        self.peso = 0
        self.altura = 0
        self.mensalidade = 120.00
 
    def inserirDados(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
 
    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        print("IMC do aluno:", imc)
 
    def obter_valor_mensalidade(self):
        if self.idade < 18:
            desconto = self.mensalidade * 0.2
            valor_final = self.mensalidade - desconto
            print("Mensalidade com desconto (menor de idade):", valor_final)
        else:
            print("Mensalidade:", self.mensalidade)
 
 
aluno = AlunoAcademia()
nome = input("Insira o nome do aluno: ")
idade = int(input("Insira a idade do aluno: "))
peso = float(input("Insira o peso do aluno (kg): "))
altura = float(input("Insira a altura do aluno (m): "))
aluno.inserirDados(nome, idade, peso, altura)
 
aluno.calcular_imc()
aluno.obter_valor_mensalidade()