# Devuelve un objeto de mapa (que es un iterador) de los resultados después de aplicar la función dada a cada elemento de un iterable dado 

# 2 Parámetros - Función, Iterador
numeros = [1,2,3,4,5]

def square(num):
  result = num**2
  return result

for item in map(square, numeros):
  print(item)
print("")
# Mapear una lista
numeros = [1,2,3,4,5]

def square(num):
  result = num**2
  return result

lista = list(map(square, numeros))
for item in lista: ""

print(lista); print("")
# Debemos poner un iterable por cada parámetro, los cuales se emparejarán
numeros = [1,2,3,4,5]

def square(num, saludo, digitos):
  result = num**2
  return result, saludo, digitos

for item in map(square, numeros, "Hola", (1,2,3,4)): print(item)
print("")