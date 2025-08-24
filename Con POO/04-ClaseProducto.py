'''
Crea una clase Producto con atributos nombre y precio, y un método para mostrar el precio con IVA (21%).
'''
class Producto:
    def __init__(self, nombre:str, precio:float):
        self.nombre = nombre
        self.precio = precio

    def precioIva(self):
        iva = 0.21
        precioFinal = (self.precio * iva) + self.precio
        print(f"El producto: '{self.nombre}' tiene un precio de '{self.precio}' y sumandole el '{iva}' de iva, tiene un precio final de: '{precioFinal:.2f}'")

producto1 = Producto("Sudadera", 35.60)
producto1.precioIva()