# Formar de crear una función

# Sin Parámetros
def saludo():
  print("Hola"); print("¿Cómo estás?")

saludo()

# Con Parámetros
def suma(a, b):
  total = a + b; print(total)

suma(7, 8)

# Función con retorno
total = 0

def suma_potencia_10(a, b):
  global total
  total = a + b
  total = total ** 10
  return total

suma_potencia_10(10, 3)
print(total)