# Lista de pares a partir de otra lista creada con las potencias de 2 de los primeros 10 números

# Método tradicional
lista = []
for numero in range(0,11):
    lista.append(numero**2)

pares = []   
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

# Con comprensión de listas
lista = [numero for numero in 
            [numero**2 for numero in range(0,11)] 
                if numero % 2 == 0]
print(lista)