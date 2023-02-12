# Crea un objeto set
set2 = set(); print(set2)

# Set con un elemento
set3 = set(); set3.add(1); print(set3)

# Set con muchos elementos
set4 = set({1, 2, 3, 4, 5, 6, 7}); print(set4)

set4 = set(); set4.add(1); set4.add(2); set4.add(3); set4.add(4); set4.add(5)
set4.add(6); set4.add(7); print(set4)

# Al asignarle una cadena directamente al método set(), dividirá la cadena por caracteres de manera desordenada
set5 = set("Hola Mundo"); print(set5)

# Convertir una colección a set -- 1 Parámetro
diccionario = {1: "Uno", 2: "Dos"}
lista = [1, 2, 3, 4]
tupla = (1, 2, 3, 4, 5)

mi_set = set(diccionario); print(mi_set)
mi_set = set(lista); print(mi_set)
mi_set = set(tupla); print(mi_set)