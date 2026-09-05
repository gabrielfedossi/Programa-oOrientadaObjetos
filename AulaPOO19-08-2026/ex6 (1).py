class Funcionario:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.pontos = []

    def bater_ponto(self, presente):
        self.pontos.append(presente)

        if presente == 1:
            print(f"{self.nome} bateu o ponto.")
        else:
            print(f"{self.nome} não bateu o ponto.")


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario, comissao):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao

    def bater_meta(self):
        print(f"{self.nome} bateu a meta de vendas!")


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario, senha):
        super().__init__(nome, matricula, salario)
        self.senha = senha

    def acessar_sistema(self):
        print(f"{self.nome} acessou o sistema como gerente.")


vendedor = Vendedor("João", 101, 2500, 10)
vendedor.bater_ponto(1)
vendedor.bater_meta()

gerente = Gerente("Carlos", 102, 6000, "1234")
gerente.bater_ponto(1)
gerente.acessar_sistema()
