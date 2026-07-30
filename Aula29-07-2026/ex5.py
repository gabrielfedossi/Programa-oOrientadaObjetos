class Funcionario:
    def __init__(self):
        self.nome = None
        self.sobrenome = None
        self.horas_trabalhadas = 0
        self.valor_hora = 0
 
    def inserirDados(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
 
    def nomeCompleto(self):
        print(self.nome + " " + self.sobrenome)
 
    def calcularSalario(self):
        salario = self.horas_trabalhadas * self.valor_hora
        print("Salário do mês:", salario)
 
    def incrementarHoras(self, horas):
        self.horas_trabalhadas += horas
        print("Novo total de horas trabalhadas:", self.horas_trabalhadas)
 
 
funcionario = Funcionario()
nome = input("Insira o nome do funcionário: ")
sobrenome = input("Insira o sobrenome do funcionário: ")
horas_trabalhadas = float(input("Insira a quantidade de horas trabalhadas: "))
valor_hora = float(input("Insira o valor da hora trabalhada: "))
funcionario.inserirDados(nome, sobrenome, horas_trabalhadas, valor_hora)
 
funcionario.nomeCompleto()
funcionario.calcularSalario()
 
horas_extra = float(input("Insira a quantidade de horas a incrementar: "))
funcionario.incrementarHoras(horas_extra)
