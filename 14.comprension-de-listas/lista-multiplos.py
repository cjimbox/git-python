# Lista con los todos los múltiples de 2 entre 0 y 10

### Método tradicional
lista = []
for numero in range(0,11):
    if numero % 2 == 0:
        lista.append(numero)
print(lista)

### Con comprensión de listas
lista = [numero for numero in range(0,11) if numero % 2 == 0]
print(lista)