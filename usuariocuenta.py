#codigo cuenta bancaria de mi core anterior#
class Cuentabancaria:
   
   def __init__(self,balancedecuenta,interes):
     self.balancedecuenta = 0
     self.interes= 0
   def deposito(self,monto):
     self.balancedecuenta += monto
   def retiro(self, monto):
     if (self.balancedecuenta-monto) < 0:
      print("Fondos insuficientes, cobrando una tarifa de 5 dolares")
      self.balancedecuenta -= 5
     else:
      self.balancedecuenta -= monto
   def mostrar_info_cuenta(self):
     return f"{self.balancedecuenta}"

   def generar_interes(self):
      self.interes += (self.balancedecuenta*1/100)

#nuevo codigo para enlazar con este core

class Usuario:
   def __init__(self,nombre,email):
    self.nombre = nombre
    self.email = email
    self.cuenta = {

        "Ahorrosuniversitarios": Cuentabancaria(0,0),
        "Ahorrosdecasa": Cuentabancaria(0,0)
        
    }
   def mostrar_cuentas(self):
    print(f"Usuario:{self.nombre}, Ahorros Universitarios: {self.cuenta['Ahorrosuniversitarios'].mostrar_info_cuenta()}, Ahorros de casa: {self.cuenta['Ahorrosdecasa'].mostrar_info_cuenta()}")

#el core me pide actualizar el método hacer_depósito, hacer retiro, mostrar balance de la clase Usuario pero todo eso lo tengo en la clase Cuentabancaria y el core me dice que no debo cambiar nada de cuentabancaria.
#actualizacion tuve que cambiar el codigo de core de mi anterior ejercicio mostrar_info_cuenta de print a return pues no encontraba la forma de que imprimA sin modificarlo 
Kloe=Usuario("Kloe", "señoritakloe@pacman.com")

Kloe.cuenta["Ahorrosdecasa"].deposito(300)
Kloe.cuenta["Ahorrosuniversitarios"].deposito(400)
Kloe.cuenta["Ahorrosuniversitarios"].retiro(300)
Kloe.mostrar_cuentas()
