# Agrega un contador a un iterable y lo devuelve en forma de objeto de enumeración (posición: valor)

# Recorrer una cadena - 1 Parámetro (iterable)
palabra = "Hola"

for letter in enumerate(palabra):
  print(letter)

# Desempaquetar una cadena de texto
for index, letter in enumerate("Mundo"):
  print(index, letter, end=" ")
print("")   

# Cambiar la posición del contador - 2 Parámetros (iterable, contador)
for enumeracion in enumerate("Hola", 2):
  print(enumeracion)

# Crear una lista de tuplas
lista = list(enumerate("Hola", 2))
print(lista); print(lista[2])