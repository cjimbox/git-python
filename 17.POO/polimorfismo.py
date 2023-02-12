# Heredamos de la clase y sobre escribimos el método
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
  def quien_soy(self):
    print("Soy un perro")
    

miPerro = Perro()
miPerro.quien_soy()