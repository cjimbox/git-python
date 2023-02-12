# Ordena una lista de forma ascendente y retorna una nueva lista
mi_lista = [4, 3, 2, 1]; nueva_lista = sorted(mi_lista)
print(mi_lista); print(nueva_lista); print("")

# Tuple
x = ('q', 'w', 'e', 'r', 't', 'y')
print(sorted(x))
  
# String-sorted based on ASCII translations
x = "python"
print(sorted(x))
  
# Dictionary
x = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6}
print(sorted(x))
  
# Set
x = {'q', 'w', 'e', 'r', 't', 'y'}
print(sorted(x))
  
# Frozen Set
x = frozenset(('q', 'w', 'e', 'r', 't', 'y'))
print(sorted(x))

# Ordenar de manera ascendente por el valor de la posición 1 de cada lista
def take_second(elem):
  return elem[1]

print(""); random = [(2,2), (3,4), (4,1), (1,3)]
sorted_list = sorted(random, key=take_second)
print(sorted_list, end="\n\n")

# Por el primer valor
def take_second(elem):
  return elem

random = [(2,2), (3,4), (4,1), (1,3)]
sorted_list = sorted(random, key=take_second)
print(sorted_list, end="\n\n")

# Ordenar de forma descendente
mi_lista = [192, 1, 1927, 1092, 2, 29, 1029]
nueva_lista = sorted(mi_lista, reverse=True)
print(mi_lista); print(nueva_lista); print("")