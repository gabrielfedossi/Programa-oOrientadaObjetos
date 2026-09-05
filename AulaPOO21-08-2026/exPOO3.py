class Usuario:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")


class Cliente(Usuario):
    def __init__(self, *args, endereco, ponto_referencia=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.endereco = endereco
        self.ponto_referencia = ponto_referencia

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Endereço: {self.endereco}")
        if self.ponto_referencia:
            print(f"Ponto de referência: {self.ponto_referencia}")


class Entregador(Usuario):
    def __init__(self, *args, veiculo, placa, avaliacao_inicial=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.veiculo = veiculo
        self.placa = placa
        self.avaliacao_inicial = avaliacao_inicial

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Veículo: {self.veiculo}")
        print(f"Placa: {self.placa}")
        if self.avaliacao_inicial is not None:
            print(f"Avaliação inicial: {self.avaliacao_inicial}")


def registrar_pedido(nome_cliente, *itens, **info_adicional):
    quantidade = len(itens)
    itens_texto = ", ".join(itens)

    resumo = f"Pedido de {nome_cliente}: {quantidade} itens ({itens_texto})"

    if info_adicional:
        partes = []
        for chave, valor in info_adicional.items():
            partes.append(f"{chave}: {valor}")
        resumo = resumo + " — " + ", ".join(partes)

    return resumo


def criar_usuario(tipo, **dados):
    if tipo == "cliente":
        return Cliente(**dados)
    elif tipo == "entregador":
        return Entregador(**dados)
    else:
        raise ValueError("Tipo de usuário inválido. Use 'cliente' ou 'entregador'.")


if __name__ == "__main__":

    print("Clientes")
    cliente1 = Cliente("Maria Silva", "maria@email.com", "67 91234-5678",
                        endereco="Rua das Flores, 123",
                        ponto_referencia="perto do mercado")

    cliente2 = Cliente(nome="João Souza", email="joao@email.com",
                        telefone="67 98765-4321", endereco="Av. Central, 500")

    cliente1.mostrar_dados()
    print()
    cliente2.mostrar_dados()

    print("\n--- Entregadores ---")
    entregador1 = Entregador("Carlos Lima", "carlos@email.com", "67 99999-0001",
                              veiculo="moto", placa="ABC1D23", avaliacao_inicial=4.8)

    entregador2 = Entregador(nome="Ana Paula", email="ana@email.com",
                              telefone="67 98888-0002", veiculo="bicicleta",
                              placa="N/A")

    entregador1.mostrar_dados()
    print()
    entregador2.mostrar_dados()

    print("\n--- Pedidos ---")
    print(registrar_pedido("Maria", "pizza", "refrigerante",
                            pagamento="pix", desconto="10%"))

    print(registrar_pedido("João", "hamburguer"))

    print(registrar_pedido("João", "marmita", "suco",
                            observacao="deixar na portaria"))

    print("\n--- Fábrica de usuários ---")
    novo_cliente = criar_usuario(
        "cliente",
        nome="Beatriz Alves", email="bia@email.com", telefone="67 97777-0003",
        endereco="Rua Nova, 45", ponto_referencia="portão azul"
    )
    novo_entregador = criar_usuario(
        "entregador",
        nome="Rafael Souza", email="rafael@email.com", telefone="67 96666-0004",
        veiculo="carro", placa="XYZ9K88"
    )

    novo_cliente.mostrar_dados()
    print()
    novo_entregador.mostrar_dados()