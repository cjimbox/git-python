# Devuelve un objeto de vista con las claves de un diccionario
mi_diccionario = {1: "Uno", 2: "Dos"}
print(mi_diccionario)
print(mi_diccionario.keys())
x = mi_diccionario.keys()
print(x)

# El objeto se actualiza con cada nueva llave añadida (no importa si el objeto fue instanciado antes)
mi_diccionario[3] = "Tres"; print(x)