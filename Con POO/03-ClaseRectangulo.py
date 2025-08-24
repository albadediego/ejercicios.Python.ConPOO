'''
Crea una clase Rectangulo con atributos ancho y alto, y un método que calcule el área.
'''
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def calcularArea(self):
        area = self.ancho * self.alto
        print(f"El area del rectangulo de '{self.ancho}' de ancho y '{self.alto}' de alto es de: {area}")

rectangulo1 = Rectangulo(3,5)
rectangulo1.calcularArea()

    