class Brinquedo:
    def __init__(self, nome, cor, tamanho, preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        print(f"Estou brincando com {self.nome}")


class Buzz(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está voando!")


class Woody(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está laçando!")


class Carrinho(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está andando!")


class Boneca(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está sendo vestida!")


class Robo(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está andando e falando!")


class Dinossauro(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está rugindo!")


class Aviao(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está voando!")


class Barco(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está navegando!")


class Bola(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está quicando!")


class Trem(Brinquedo):
    def brincar(self):
        print(f"{self.nome} está andando pelos trilhos!")


brinquedos = [
    Buzz("Buzz Lightyear", "Branco", "Grande", 100),
    Woody("Woody", "Amarelo", "Médio", 80),
    Carrinho("Relâmpago", "Vermelho", "Pequeno", 50),
    Boneca("Barbie", "Rosa", "Médio", 70),
    Robo("Robo X", "Azul", "Grande", 120),
    Dinossauro("Rex", "Verde", "Grande", 90),
    Aviao("Aviãozinho", "Azul", "Pequeno", 40),
    Barco("Barquinho", "Branco", "Médio", 60),
    Bola("Bola", "Vermelha", "Médio", 30),
    Trem("Thomas", "Azul", "Grande", 100)
]

for brinquedo in brinquedos:
    brinquedo.brincar()
