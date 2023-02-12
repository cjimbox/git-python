# Crear una clase
class Perro():

  def __init__(self, raza, nombre, puntos):

    self.raza = raza
    self.nombre = nombre
    self.puntos = puntos


husky = Perro("Husky", "Max", False)
print(type(husky))

# Clase sin atributos
class Gato():

  def __init__(self):

    print("Hola soy un gato")


botas = Gato()
print(type(botas))

# Crear una clase con atributos y métodos
class Animal():
  # Creación de atributos
  def __init__(self, tipo, comida):

    self.tipo = tipo
    self.comida = comida
    print("Animal creado")
  # Creación de métodos
  def quien_soy(self, tipo):
    print(f"Soy un {tipo}")
  def comer(self, comida):
    print(f"Me gusta comer {comida}")

animalDesconocido = Animal("Perro", "Croquetas")
print(animalDesconocido.tipo)
print(animalDesconocido.comida)
animalDesconocido.quien_soy("Perro")