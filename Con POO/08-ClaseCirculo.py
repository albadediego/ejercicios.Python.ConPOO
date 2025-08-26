'''
Crea una clase Circulo con un atributo radio y métodos para calcular área y perímetro.
'''
from math import pi

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        area = pi * self.radio ** 2
        print(f"El area del circulo es de {area:.2f}")

    def perimetro(self):
        perimetro = 2 * pi * self.radio
        print(f"El perimetro del circulo es de {perimetro:.2f}")

circulo1 = Circulo(9)
circulo1.area()
circulo1.perimetro()