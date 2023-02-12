# Devuele el valor más pequeño de un iterable 

# 1 Parámetro
lista = [200, 2, 1000, 192]
print(min(lista))

# Iterar una lista de cadena (evalúa la primera letra)
cadena = ["Hola", "Mundo", "z"]
print(min(cadena))

# Iterables - Más de un parámetro
lista = [200, 192, 10282, 181, 282293, 1]
lista2 = [9, 192, 3]
lista3 = [92, 19, 2, 912, 12]
print(min(lista, lista2, lista3))

# Función para definir como se va a comparar
def minimo(elem):
  return elem[1]

lista = [(1,2),(3,4),(5,6),(7,8)]
print(min(lista, key=minimo))

# Función para buscar el que tenga la longitud más pequeña
def longitud(elem):
  return len(elem)

lista = ["Hola", "Mundo", "Jimmy", "a"]
print(min(lista, key=longitud))

# Valor predeterminado si el iterable está vacío
lista = []
print(min(lista, default=1))