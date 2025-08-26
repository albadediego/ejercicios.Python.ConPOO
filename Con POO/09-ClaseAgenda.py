'''
Crea una clase Agenda que permita añadir, buscar y listar contactos.
'''
class Agenda:
    def __init__(self, listaContactos:list):
        self.listaContactos = listaContactos
    
    def aniadir(self, nombre, telefono):
        contacto = {'nombre':nombre, 'telefono':telefono}
        self.listaContactos.append(contacto)
        print(f"Contacto '{nombre}' añadido correctamente")

    def buscar(self, nombre):
        for contacto in self.listaContactos:
            if contacto['nombre'] == nombre:
                print(f"Contacto encontrado: {contacto}")
                return contacto
        print(f"Contacto no encontrado")

    def mostrarTodos(self):
        if not self.listaContactos:
            print("No existen contactos en la agenda")
        print("----Lista de contactos----")
        for i in range(len(self.listaContactos)):
            contacto = self.listaContactos[i]
            print(f"{i+1}. Nombre: {contacto['nombre']}, Telefono: {contacto['telefono']}")

agenda1 = Agenda([])

agenda1.aniadir("Ana Garcia", "612345678")
agenda1.aniadir("Luis Perez", "987654321")
agenda1.aniadir("Sofia Lopez", "112233445")

agenda1.buscar("Ana Garcia")
agenda1.buscar("Jose Antonio")

agenda1.mostrarTodos()
