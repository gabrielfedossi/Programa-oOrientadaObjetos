class Ingresso:
    def __init__(self, preco, setor):
        self.preco = preco
        self.setor = setor

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco

    def mostrar_setor(self):
        print(f"Setor: {self.setor}")


class IngressoVIP(Ingresso):
    def __init__(self, preco, setor, camarote, open_bar, open_food, estacionamento):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento

    def pegar_bebida(self):
        if self.open_bar:
            print("Bebida liberada!")
        else:
            print("Bebida não disponível.")

    def acessar_camarote(self):
        if self.camarote:
            print("Acesso ao camarote liberado!")
        else:
            print("Acesso ao camarote não disponível.")


ingresso = IngressoVIP(300, "VIP", True, True, True, True)
ingresso.mostrar_setor()
ingresso.pegar_bebida()
ingresso.acessar_camarote()
