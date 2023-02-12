# Crear una función anidada
nombre = "Variable Global"

def saludo():
  nombre = "Jimmy"

  def hola():
    print("Hola", nombre)

  hola()

saludo()