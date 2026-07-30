class Agenda:
    def __init__(self):
        self.dia = 0
        self.mes = 0
        self.ano = 0
        self.anotacao = None
 
    def validar_data(self, dia, mes, ano):
        if dia < 1 or dia > 31:
            print("Dia inválido!")
            return False
        if mes < 1 or mes > 12:
            print("Mês inválido!")
            return False
        if ano < 0:
            print("Ano inválido!")
            return False
        self.dia = dia
        self.mes = mes
        self.ano = ano
        return True
 
    def anotar_tarefa(self, anotacao):
        self.anotacao = anotacao
        print("Tarefa anotada com sucesso!")
 
    def mostrar_anotacao(self):
        print("Data:", self.dia, "/", self.mes, "/", self.ano)
        print("Anotação:", self.anotacao)
 
 
agenda = Agenda()
dia = int(input("Insira o dia: "))
mes = int(input("Insira o mês: "))
ano = int(input("Insira o ano: "))
 
if agenda.validar_data(dia, mes, ano):
    anotacao = input("Insira a anotação da tarefa: ")
    agenda.anotar_tarefa(anotacao)
    agenda.mostrar_anotacao()