# Crear una función lambda
numeros = [1,2,3,4,5,6,7]

square = lambda num: print(num**2)

square(5)

# Usando map()
numeros = [1,2,3,4,5,6,7]

print(list(map(lambda num: num ** 2, numeros)))

# Usando filter()
numeros = [1,2,3,4,5,6,7]

print(list(filter(lambda num: num % 2 == 0, numeros)))