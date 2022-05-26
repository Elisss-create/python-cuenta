class Cuenta: 
  def __init__(self, titular:"Eliana", cantidad=0):
    self.titular = titular
    self.cantidad = cantidad

  def mostrar(self):
    print ("Titular:",self.titular,"  Cantidad:",self.cantidad)

  def ingresar_monto(self,cantidad):
    self.cantidad+=cantidad
    print(f"Ingreso {cantidad}")
    print("Total es $",self.cantidad)
  
  def retirar(self,cantidad):
    self.cantidad-=cantidad
    print("se retira $",cantidad, " Saldo $", self.cantidad)

cuenta1=Cuenta("Cecilia",2000)
cuenta1.mostrar()
cuenta1.ingresar_monto(3000)
cuenta1.retirar(1000)
