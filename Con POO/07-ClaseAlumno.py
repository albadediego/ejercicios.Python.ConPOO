'''
Crea una clase Alumno con atributos nombre y notas (lista), y un método para calcular la media.
'''
class Alumno:
    def __init__(self, nombre, notas:list):
        self.nombre = nombre
        self.notas = notas
    
    def calcularMedia(self):
        sumaNotas = sum(self.notas)
        cantidadNotas = len(self.notas)
        media = sumaNotas / cantidadNotas
        print(f"La nota media de '{self.nombre}' es de {media}")

alumno1 = Alumno("Ana", [6,9,7,6,8])
alumno1.calcularMedia()

