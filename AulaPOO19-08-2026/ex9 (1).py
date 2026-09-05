class Compra:
    def __init__(self, numero, produto, valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0

    def calcular_valor_total(self):
        icms = self.valor * 0.17
        frete = self.valor * 0.05
        self.valor_total = self.valor + icms + frete
        return self.valor_total


class Avista(Compra):
    def __init__(self, numero, produto, valor, desconto):
        super().__init__(numero, produto, valor)
        self.desconto = desconto

    def preco_com_desconto(self):
        valor_total = self.calcular_valor_total()
        desconto = valor_total * (self.desconto / 100)
        return valor_total - desconto


class Parcelada(Compra):
    def __init__(self, numero, produto, valor, numero_parcelas):
        super().__init__(numero, produto, valor)
        self.numero_parcelas = numero_parcelas

    def valor_parcelas(self):
        valor_total = self.calcular_valor_total()
        return valor_total / self.numero_parcelas


compra1 = Avista(1, "Notebook", 3000, 10)
print(f"Preço à vista: R$ {compra1.preco_com_desconto():.2f}")

compra2 = Parcelada(2, "Celular", 2000, 5)
print(f"Valor de cada parcela: R$ {compra2.valor_parcelas():.2f}")
