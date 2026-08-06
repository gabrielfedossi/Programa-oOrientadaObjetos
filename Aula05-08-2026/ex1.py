class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhaCompra:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto : Produto):
        self.produtos.append(produto)
        print(f"Produto {produto.nome} adicionado!\n")

    def calcular_preco(self) -> float:
        soma = 0

        for p in self.produtos:
            soma += p.preco

        return soma

    def remover_produto(self, indice):
        if 0 <= indice < len(self.produtos):
            produto = self.produtos.pop(indice)
            print(f"Produto {produto.nome} removido!")
        else:
            print("Índice inválido.")

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.carrinho = CarrinhaCompra()


    def finalizar_pedido(self):
        total = self.carrinho.calcular_preco()
        print(f"Pedido finalizado, valor total: R${total}")

