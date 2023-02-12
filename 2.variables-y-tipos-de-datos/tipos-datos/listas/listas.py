# Listas
lista = ["Jimmy", 2005, "Septiembre"]; print(lista)

# Indexado
print(lista[2])

# Slicing
print(lista[1:])

# Sumar listas
lista2 = ["P", 900, True]; mega_lista = lista + lista2
print(mega_lista)

# Sumar elementos
mi_lista = [2, "Hola", 29209]; mi_lista2 = ["Mundo", 9012, False, 1]
suma_elementos_lista = mi_lista[1] + " " + mi_lista2[0]
print(suma_elementos_lista)

# Mutables
mi_lista[0] = "Modificado"; print(mi_lista[0])