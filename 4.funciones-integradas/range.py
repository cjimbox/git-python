# Devuelve una secuencia inmutable de números que se pueden convertir fácilmente en listas, tuplas, conjuntos, etc.

# Crear una secuencia del 0 al 10 - 1 Parámetro (stop)
for num in range(10):
  print(num, end=" ")
print("")

# Crear una secuencia del 0 al 11 y que de 2 pasos - 3 Parámetros (start, stop, step)
for num in range(0, 11, 2):
  print(num, end=" ")
print("")

# Guardar y convertir el rango en una lista
lista = list(range(0, 11, 2))

for num in lista:
  print(num, end=" ")
print(""); print(lista)

# 2 Parámetros (start, stop)
for num in range(0,10):
  print(num, end=" ")
