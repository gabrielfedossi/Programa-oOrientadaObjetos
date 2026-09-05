class Filme:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def play(self):
        print(f"Foi dado play no filme {self.nome}")


class Acao(Filme):
    def explodir(self):
        print(f"O filme {self.nome} teve uma explosão!")


class Drama(Filme):
    def emocionar(self):
        print(f"O filme {self.nome} deixou todos emocionados!")


class Suspense(Filme):
    def assustar(self):
        print(f"O filme {self.nome} deixou todos assustados!")


filme1 = Acao("Vingadores", 150)
filme2 = Drama("À Procura da Felicidade", 117)
filme3 = Suspense("Invocação do Mal", 112)

filme1.play()
filme1.explodir()
filme2.play()
filme2.emocionar()
filme3.play()
filme3.assustar()
