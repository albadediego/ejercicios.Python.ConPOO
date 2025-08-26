'''
Crea una clase CuentaBancaria con métodos para depositar, retirar y mostrar el saldo.
'''
class CuentaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se ha añadido correctamente")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se ha retirado correctamente")
        else:
            print(f"No dispone de saldo suficiente")

    def mostrarSaldo(self):
        print(f"El saldo actual de la cuenta es de {self.saldo} euros")

cuenta1 = CuentaBancaria()
cuenta1.depositar(150)
cuenta1.mostrarSaldo()
cuenta1.retirar(100)
cuenta1.mostrarSaldo()
cuenta1.retirar(200)