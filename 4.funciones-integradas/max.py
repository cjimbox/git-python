# Devuele el valor más grande de un iterable 

# 1 Parámetro
lista = [200, 2, 1000, 192]
print(max(lista))

# Iterar una lista de cadena (evalúa la primera letra)
cadena = ["Hola", "Mundo", "z"]
print(max(cadena))

# Iterables - Más de un parámetro
lista = [200, 192, 10282, 181, 282293, 1]
lista2 = [9, 192, 3]
lista3 = [92, 19, 2, 912, 12]
print(max(lista, lista2, lista3))

# Función para definir como se va a comparar
def maximo(elem):
  return elem[1]

lista = [(1,2),(3,4),(5,6),(7,8)]
print(max(lista, key=maximo))

# Función para buscar el que tenga la longitud más pequeña
def longitud(elem):
  return len(elem)

lista = ["Hola", "Mundo", "Jimmy", "a"]
print(max(lista, key=longitud))

# Valor predeterminado si el iterable está vacío
lista = []
print(max(lista, default=1000))