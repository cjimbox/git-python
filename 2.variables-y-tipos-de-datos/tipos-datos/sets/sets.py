# Sets
sets = {1, "Hola", False, "w", "z", "a"}
print(sets)

# Crear un set sin elementos
set2 = set(); print(set2)

# Set con un elemento
set3 = {1}; print(set3)

set3 = set(); set3.add(1); print(set3)

# Set con muchos elementos
set4 = {1, 2, 3, 4, 5, 6, 7}; print(set4)

set4 = set({1, 2, 3, 4, 5, 6, 7}); print(set4)

set4 = set(); set4.add(1); set4.add(2); set4.add(3); set4.add(4); set4.add(5)
set4.add(6); set4.add(7); print(set4)

# No se guardan los valores duplicados
mi_set = {1, 1, 1, 2, 3, 4}; print(mi_set)

# Cadenas en sets
set5 = {"Hola", 3, 4, "Mundo"}; print(set5)

# Al asignarle una cadena directamente al método set(), dividirá la cadena por caracteres de manera desordenada
set5 = set("Hola Mundo"); print(set5)

# Quitar los valores repetidos de una lista
lista = [1,1,1,2,3,3,3,4,4,4,1,4,23] 
setl = set(lista) 
lista = list(setl)
print(lista)