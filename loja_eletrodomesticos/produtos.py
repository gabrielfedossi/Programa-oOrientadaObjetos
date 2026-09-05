class Produto:
    def __init__(self, id, nome, categoria, preco, estoque, garantia):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque
        self.garantia = garantia


    def preco(self):
        return self.preco

    def alterar_preco(self, novo_preco):
        if novo_preco <= 0:
            raise ValueError("Insira um valor válido")
        self.preco = novo_preco

    def estoque(self):
        return self.estoque

    def add_estoque(self, qtd):
        if qtd <= 0:
            raise ValueError("Insira um valor válido")

        self.estoque += qtd

    def remover_estoque(self, qtd):
        if qtd <= 0:
            raise ValueError("Insira um valor válido")

        if qtd > self.estoque:
            raise ValueError(f"O estoque nao tem essa quantidade para o produto {self.nome}")

        self.estoque -= qtd


    def descricao(self):
        return f"{self.nome} - CATEGORIA: {self.categoria}"

class LinhaBranca(Produto):
    def __init__(self, id, nome, categoria, preco, estoque, garantia, consumokwh, eficiencia):
        super().__init__(id, nome, categoria, preco, estoque, garantia)

        self.consumokwh = consumokwh
        self.eficiencia = eficiencia

    def descricao(self):
        return (
            f"{self.nome} - Linha Branca | "
            f"Consumo: {self.consumokwh} kwh |"
            f"Eficiencia : {self.eficiencia}"
        )

class Eletroportatil(Produto):
    def __init__(self, id, nome, categoria, preco, estoque, garantia, volts):
        super().__init__(id, nome, categoria, preco, estoque, garantia)
        self.volts = volts


    def descricao(self):
        return (
            f"{self.nome} - Eletroportatil |"
            f"Voltagem: {self.volts}"
        )




        


