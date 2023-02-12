# Crear una lista con las letras de una palabra

### Método tradicional
lista = []

for letra in "casa":
  lista.append(letra)
print(lista)

### Con comprensión de listas
lista = [letra for letra in "casa"]
print(lista)