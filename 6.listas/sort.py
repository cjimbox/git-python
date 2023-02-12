# Ordenar una lista de forma ascendente -- No soporta la combinación de varios tipos de datos 
str_lista = ["Hola", "Abedul", "z", "Carlos", "Metro"]
num_lista = [1000, 9, 182, 1827272, 0, 6]

str_lista.sort(); print(str_lista)
num_lista.sort(); print(num_lista); print("")

# Lista Descendente - 1 Parámetro
str_lista.sort(reverse = True); num_lista.sort(reverse = True)
print(str_lista); print(num_lista); print("")

# Función que sirve como clave para la comparación de clasificación, se ordena respecto a lo que retorna la función - 2 Parámetros
def MyFunc(e):
  return e["year"]

carros = [
  {"car": "Ford", "year": 2005},
  {"car": "Mitsubishi", "year": 2000},
  {"car": "BMW", "year": 2019},
  {"car": "VW", "year": 2011}
]

carros.sort(key = MyFunc); print(carros); print("")

# Otro ejemplo
def Clientes(nombre):
  return nombre["cliente"]

clientes = [
  {"cliente": "Jimmy", "edad": 2005},
  {"cliente": "Rolly", "edad": 2011},
  {"cliente": "Kevin", "edad": 2000},
  {"cliente": "Geovany", "edad": 2019}
]

clientes.sort(key = Clientes); print(clientes); print("")