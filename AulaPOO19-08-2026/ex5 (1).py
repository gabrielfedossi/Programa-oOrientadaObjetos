class Pessoa:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar(self):
        print(f"{self.nome} está negociando.")


class Fisica(Pessoa):
    def __init__(self, cpf, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cpf = cpf

    def comprar(self):
        print(f"{self.nome} realizou uma compra.")


class Juridica(Pessoa):
    def __init__(self, cnpj, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cnpj = cnpj

    def emitir_nota(self):
        print(f"{self.nome} emitiu uma nota fiscal.")


pessoa1 = Fisica("123.456.789-00","Gabriel", "92219-9999", "gabrielf@gmail.com", endereco="Rua A")
pessoa1.negociar()
pessoa1.comprar()

pessoa2 = Juridica("3333-3333","Empresa X", "empresaasdsda@gmail.com", "Rua B", "12.345.678/0001-00")
pessoa2.negociar()
pessoa2.emitir_nota()
print(pessoa1.telefone)
