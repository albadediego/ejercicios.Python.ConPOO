'''
Crea una clase Coche con atributos marca y modelo, y un método que muestre la información del coche.
'''
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrarInformacion(self):
        print(f"El coche es de la marca: '{self.marca}' y modelo: '{self.modelo}'")

coche1 = Coche("Peugeot", "307sw")
coche1.mostrarInformacion()