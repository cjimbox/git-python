# Lista con las potencias de 2 de los primeros 10 números

### Método tradicional
lista = []
for numero in range(0,11):
    lista.append(numero**2)
print(lista)

### Con comprensión de listas
lista = [numero**2 for numero in range(0,11)]
print(lista)