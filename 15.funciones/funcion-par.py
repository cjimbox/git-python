# Función para ver si al menos un número es par en una lista
def num_par(num_lista):
  for number in num_lista:
    if number % 2 == 0:
      print(True) 
    else:
      pass
  print(False)

num_par([1, 3, 10])