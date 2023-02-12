# Iterar una lista
lista = [1,2,3,4,5]

for elem in lista: print(f"{elem}: {lista}")
print("")

# Iterar una cadena de caracteres
cadena = "Hola Mundo"

for letra in cadena: print(letra)
print("")

# Iterar un diccionario
diccionario = {"Saludo": "Hola", "Despedida": "Adiós"}

for key in diccionario:
  print(key)
print("")

# Ver todos los items de un diccionario en un ciclo
for item in diccionario.items():
  print(item)
print("")

# Desempaquetar un diccionario
for key, value in diccionario.items():
  print(key); print(value)
print("")

# Iterar una tupla
tupla = (1,2,3,4,5)

for elem in tupla:
  print(elem)
print("")

# Imprimir un item de una lista
lista = [(1,2),(3,4),(5,6)]

for item in lista:
  print(item)
print("")

# Desempaquetar una tupla
lista = [(1,2),(3,4),(5,6),(7,8)]

for (a,b) in lista:
  print(a, b)
print("")