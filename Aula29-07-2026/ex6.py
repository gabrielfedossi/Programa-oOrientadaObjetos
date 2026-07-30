class Circulo:
    PI = 3.1415
 
    def __init__(self):
        self.raio = 0
 
    def inserirDados(self, raio):
        self.raio = raio
 
    def imprimir_raio(self):
        print("Raio:", self.raio)
 
    def calcular_area(self):
        area = Circulo.PI * (self.raio ** 2)
        print("Área do círculo:", area)
 
    def calcular_circunferencia(self):
        circunferencia = 2 * Circulo.PI * self.raio
        print("Circunferência do círculo:", circunferencia)
 
 
circulo = Circulo()
raio = float(input("Insira o raio do círculo: "))
circulo.inserirDados(raio)
 
circulo.imprimir_raio()
circulo.calcular_area()
circulo.calcular_circunferencia()