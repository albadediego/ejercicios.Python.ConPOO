'''
Crea una clase Libro con atributos titulo y autor, y un método para mostrar su información.
'''
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrarInformacion(self):
        print(f"El libro: '{self.titulo}' es del autor: '{self.autor}'")

libro1 = Libro("Don quijote de la mancha", "Miguel de Cervantes")
libro1.mostrarInformacion()