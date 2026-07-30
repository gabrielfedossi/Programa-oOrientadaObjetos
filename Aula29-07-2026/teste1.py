class Estudante:
    def __init__(self, nome, idade, formacao):
        self.nome = nome
        self.idade = idade
        self.formacao = formacao

    def get_grade(self):
        return self.formacao
        