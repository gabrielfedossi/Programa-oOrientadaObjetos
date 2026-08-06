class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def descricao(self):
        return f"{self.nome} ganha R$ {self.salario}"


class Professor(Funcionario):
    def __init__(self, nome, salario, disciplina):
        super().__init__(nome, salario)
        self.disciplina = disciplina

    def descricao(self):
        return f"{super().descricao()} e leciona {self.disciplina}"



prof = Professor("Fulano", 2500.0, "UC08")
print(prof.descricao())