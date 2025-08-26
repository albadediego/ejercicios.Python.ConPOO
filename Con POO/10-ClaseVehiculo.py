'''
Crea una clase Vehiculo con un método acelerar, y crea dos clases hijas (Coche y Moto) que lo sobreescriban con comportamientos distintos.
'''
class Vehiculo:
    def acelerar(self):
        print(f"El vehiculo acelera de forma generica")

class Coche(Vehiculo):
    def acelerar(self):
        print(f"El coche acelera de manera prograsiva")
    
class Moto(Vehiculo):
    def acelerar(self):
        print(f"La moto acelera de forma rapida y agil")
    
coche1 = Coche()
moto1 = Moto()

coche1.acelerar()
moto1.acelerar()