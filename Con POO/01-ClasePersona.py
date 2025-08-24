'''
Crea una clase Persona con atributos nombre y edad, y un método para presentarse.
'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentacion(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")

persona1 = Persona("Alba", 29)
persona1.presentacion()