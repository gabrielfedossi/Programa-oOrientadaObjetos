class Aluno:
    def __init__(self, nome, ra, nota1, nota2, nota3, nota4):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def mostrar_Situacao(self):
        media = ((self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4)

        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Exame"
        else:
            return "Reprovado"

        
        