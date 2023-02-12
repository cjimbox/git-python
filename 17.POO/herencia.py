# Heredamos de la clase
class Animal():
  def __init__(self):
    print("Animal creado")
  def quien_soy(self):
    print("Soy un animal")
  def comer(self):
    print("Comiendo")

class Perro():
  def __init__(self):
    Animal.__init__(self)
    print("Perro creado")
    

miPerro = Perro()
miPerro.quien_soy()