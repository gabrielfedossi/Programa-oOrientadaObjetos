class Carro:
    def __init__(self):
        self.modelo = None
        self.marca = None
        self.cor = None
        self.ano = 0
        self.valor = 0
        self.nivel = 0
        self.consumo = 0  # km rodados por litro
        self.km_rodados = 0
        self.litros_gastos_total = 0
 
    def inserirDados(self, modelo, marca, cor, ano, valor, consumo):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.consumo = consumo
 
    def abastecer(self, litros):
        self.nivel += litros
        print("Tanque abastecido! Nível atual:", self.nivel, "litros")
 
    def andar(self, km):
        self.km_rodados += km
        litros_gastos = km / self.consumo
        self.nivel -= litros_gastos
        self.litros_gastos_total += litros_gastos
        print("O carro andou", km, "km. Nível restante do tanque:", self.nivel)
 
    def verificar_nivel(self):
        if self.km_rodados > 0:
            media_gasto = self.litros_gastos_total / self.km_rodados
            print("Litros gastos por km:", media_gasto)
        else:
            print("O carro ainda não andou.")
 
    def calcular_imposto(self):
        ipva = self.valor * 0.025
        print("Valor do IPVA:", ipva)
 
 
carro = Carro()
modelo = input("Insira o modelo do carro: ")
marca = input("Insira a marca do carro: ")
cor = input("Insira a cor do carro: ")
ano = int(input("Insira o ano do carro: "))
valor = float(input("Insira o valor do carro: "))
consumo = float(input("Insira o consumo do carro (km por litro): "))
carro.inserirDados(modelo, marca, cor, ano, valor, consumo)
 
litros = float(input("Quantos litros deseja abastecer? "))
carro.abastecer(litros)
 
km = float(input("Quantos km o carro andou? "))
carro.andar(km)
 
carro.verificar_nivel()
carro.calcular_imposto()
