# Función extrae elementos de un iterable (lista, tupla, etc.) para los cuales una función devuelve True
numeros = [1,2,3,4,5,6,7]

def check_even(num):
  return num % 2 == 0

for n in filter(check_even, numeros): print(n)