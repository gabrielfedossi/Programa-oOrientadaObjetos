class Imovel:
    def __init__(self, inscricao_municipal, valor_aluguel, iptu):
        self.inscricao_municipal = inscricao_municipal
        self.valor_aluguel = valor_aluguel
        self.iptu = iptu

    def obter_parcela_IPTU(self):
        parcela = self.iptu / 12
        print(f"Parcela mensal do IPTU: R$ {parcela:.2f}")

    def set_valor_aluguel(self, novo_valor):
        self.valor_aluguel = novo_valor


class Casa(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, piscina, sala_de_estar, quartos):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.piscina = piscina
        self.sala_de_estar = sala_de_estar
        self.quartos = quartos


class Condominio(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, churrasqueira, area_lazer):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.churrasqueira = churrasqueira
        self.area_lazer = area_lazer


class Apartamento(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, quartos, elevador):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.quartos = quartos
        self.elevador = elevador


class Terreno(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, area):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.area = area


class Chacara(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu, area, piscina):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)
        self.area = area
        self.piscina = piscina


casa = Casa(123, 2000, 1200, True, True, 3)
casa.obter_parcela_IPTU()
casa.set_valor_aluguel(2200)
print(casa.valor_aluguel)
