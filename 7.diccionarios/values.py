# Devuelve un objeto de vista con los valores de un diccionario
mi_diccionario = {1: "Uno", 2: "Dos"}
print(mi_diccionario)
print(mi_diccionario.values())
x = mi_diccionario.values()
print(x)

# El objeto se actualiza con cada nuevo valor añadido (no importa si el objeto fue instanciado antes)
mi_diccionario[3] = "Tres"; print(x)