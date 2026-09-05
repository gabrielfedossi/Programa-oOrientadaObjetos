class Pessoa:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, notas):
        super().__init__(matricula, nome, idade)
        self.notas = notas
        self.media = 0

    def calcular_media(self):
        self.media = sum(self.notas) / len(self.notas)
        print(f"Média do aluno: {self.media}")

    def estudar(self):
        print(f"{self.nome} está estudando.")


class Professor(Pessoa):
    def __init__(self, matricula, nome, idade, formacao, disciplina, carga_horaria, salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.salario = salario

    def lecionar(self):
        print(f"{self.nome} está lecionando {self.disciplina}.")


aluno = Aluno(1, "Gabriel", 20, [8, 7, 9])
aluno.calcular_media()
aluno.estudar()

professor = Professor(2, "Carlos", 40, "Mestrado", "Programação", 40, 5000)
professor.lecionar()
