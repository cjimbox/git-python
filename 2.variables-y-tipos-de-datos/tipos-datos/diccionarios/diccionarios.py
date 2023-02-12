# Diccionarios
diccionario = {"Queso": "Lácteo", "Manzana": "Fruta", "Zanahoria": "Verdura"}
print(diccionario)

# Llamar una llave del diccionario
print(diccionario["Manzana"])

# Guardar listas en un diccionario
diccionario_de_listas = {
  "lista-1": [1,2,3], 
  "lista-2": [4,5,6], 
  "lista-3": [7,8,9]
}

print(diccionario_de_listas["lista-3"])

# Crear una nueva llave de un diccionario existente (se agregan al final)
nueva_llave = {1: 2, 3: 4, 5: 6}
nueva_llave[7] = 8; nueva_llave["nuevo"] = "Hola Mundo"
print(nueva_llave)

# Sobreescribir el valor de una llave
print(nueva_llave["nuevo"])
nueva_llave["nuevo"] = "Reemplazado"
print(nueva_llave["nuevo"])