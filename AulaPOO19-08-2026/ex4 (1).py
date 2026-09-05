class Passagem:
    def __init__(self, preco, assento):
        self.preco = preco
        self.assento = assento

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco

    def escolher_assento(self):
        print(f"Assento escolhido: {self.assento}")


class PassagemAviao(Passagem):
    def __init__(self, preco, assento, portao_embarque, checkin):
        super().__init__(preco, assento)
        self.portao_embarque = portao_embarque
        self.checkin = checkin

    def decolar(self):
        print("O avião está decolando!")


class PassagemBus(Passagem):
    def __init__(self, preco, assento, placa, leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito

    def abastecer(self):
        print("O ônibus está abastecendo.")


aviao = PassagemAviao(1200, "12A", "Portão 5", True)
aviao.escolher_assento()
aviao.decolar()

bus = PassagemBus(250, "20", "ABC-1234", True)
bus.escolher_assento()
bus.abastecer()
