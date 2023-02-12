# Devuelve un objeto de vista con los item de un diccionario
mi_diccionario = {1: "Uno", 2: "Dos"}
print(mi_diccionario)
print(mi_diccionario.items())
x = mi_diccionario.items()
print(x)

# El objeto se actualiza con cada nuevo item añadido (no importa si el objeto fue instanciado antes)
mi_diccionario[3] = "Tres"; print(x)