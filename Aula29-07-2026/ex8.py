class Triangulo:
    def __init__(self):
        self.ladoA = 0
        self.ladoB = 0
        self.ladoC = 0
 
    def inserirDados(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
 
    def calcular_perimetro(self):
        perimetro = self.ladoA + self.ladoB + self.ladoC
        print("Perímetro do triângulo:", perimetro)
 
    def get_maior_lado(self):
        maior = max(self.ladoA, self.ladoB, self.ladoC)
        print("Maior lado:", maior)
 
 
triangulo = Triangulo()
ladoA = float(input("Insira a medida do lado A: "))
ladoB = float(input("Insira a medida do lado B: "))
ladoC = float(input("Insira a medida do lado C: "))
triangulo.inserirDados(ladoA, ladoB, ladoC)
 
triangulo.calcular_perimetro()
triangulo.get_maior_lado()