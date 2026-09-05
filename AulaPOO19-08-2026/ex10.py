class Transporte:
    def __init__(self, nome, capacidade):
        self.nome = nome
        self.capacidade = capacidade

    def transportar(self):
        print(f"{self.nome} está realizando um transporte.")


class Terrestre(Transporte):
    def __init__(self, nome, capacidade, numero_rodas):
        super().__init__(nome, capacidade)
        self.numero_rodas = numero_rodas

    def andar(self):
        print(f"{self.nome} está andando pela estrada.")


class Automovel(Terrestre):
    def __init__(self, nome, capacidade, numero_rodas, marca):
        super().__init__(nome, capacidade, numero_rodas)
        self.marca = marca

    def dirigir(self):
        print(f"{self.nome} está sendo dirigido.")


class Aquatico(Transporte):
    def __init__(self, nome, capacidade, comprimento):
        super().__init__(nome, capacidade)
        self.comprimento = comprimento

    def navegar(self):
        print(f"{self.nome} está navegando.")


class Lancha(Aquatico):
    def __init__(self, nome, capacidade, comprimento, motor):
        super().__init__(nome, capacidade, comprimento)
        self.motor = motor

    def acelerar(self):
        print(f"{self.nome} está acelerando na água.")


class Navio(Aquatico):
    def __init__(self, nome, capacidade, comprimento, numero_containers):
        super().__init__(nome, capacidade, comprimento)
        self.numero_containers = numero_containers

    def carregar(self):
        print(f"{self.nome} está carregando containers.")


class Aereo(Transporte):
    def __init__(self, nome, capacidade, altitude_maxima):
        super().__init__(nome, capacidade)
        self.altitude_maxima = altitude_maxima

    def voar(self):
        print(f"{self.nome} está voando.")


class AviaoMonomotor(Aereo):
    def __init__(self, nome, capacidade, altitude_maxima, potencia):
        super().__init__(nome, capacidade, altitude_maxima)
        self.potencia = potencia

    def decolar(self):
        print(f"{self.nome} está decolando.")


class AviaoComercial(Aereo):
    def __init__(self, nome, capacidade, altitude_maxima, companhia):
        super().__init__(nome, capacidade, altitude_maxima)
        self.companhia = companhia

    def embarcar(self):
        print(f"Passageiros embarcando no {self.nome}.")


carro = Automovel("Carro", 5, 4, "Toyota")
lancha = Lancha("Lancha", 8, 10, 300)
navio = Navio("Navio cargueiro", 500, 200, 1000)
monomotor = AviaoMonomotor("Monomotor", 4, 5000, 180)
aviao = AviaoComercial("Boeing 737", 180, 12000, "Companhia Aérea")

carro.transportar()
carro.andar()
carro.dirigir()

lancha.transportar()
lancha.navegar()
lancha.acelerar()

navio.transportar()
navio.navegar()
navio.carregar()

monomotor.transportar()
monomotor.voar()
monomotor.decolar()

aviao.transportar()
aviao.voar()
aviao.embarcar()
