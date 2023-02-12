# Devuelve una tupla de iterables

# 1 iterable - Recorrer con un ciclo
lista = [1,2,3,4,5]
result = zip(lista)
print(result)

for item in result:
  print(item)
print("")

# 2 iterables - Convertir a un tipo de dato
lista = [1,2,3,4,5]
lista2 = ["Hola", "Mundo", "Programador"]
result = zip(lista, lista2)
mi_set = set(result)
print(mi_set); print("")

# 3 iterables
lista = [1,2,3,4,5]
lista2 = ["Hola", "Mundo", "Programador"]
lista3 = [6,7,8]
result = zip(lista, lista2, lista3)
print(result)

for item in result:
  print(item)
print("")

# Desempaquetar las tuplas
for index, index2, index3 in zip("hola", "mundo", "500"):
  print(index, end=" "); print(index2, end=" ")
  print(index3, end=" ")
print("\n")

# Crear una lista de tuplas
lista = [1,2,3,4,5]
lista2 = ["Hola", "Mundo", "Programador"]
lista3 = [6,7,8]
result = list(zip(lista, lista2, lista3))
print(result)