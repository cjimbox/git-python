# Alcance de las variables

### Variables globales
nombre = "Variable Global"

def saludo():
  nombre = "Jimmy"

  def hola():
    print("Hola", nombre)

  hola()

saludo()

### Otro ejemplo
def saludar():
  print(saludo)

saludo = "¡Hola Mundo!"
saludar()

### Variables locales
def saludar():
  saludo = "Hola"
  print(saludo)

saludar()
print(saludo)

# Una variable local actúa como variable global para las funciones anidadas dentro de su mismo contexto
def funcion_padre():
  valor = 10

  def funcion_anidada():
    valor = 20
    print(f"El valor en función anidada es: {valor}")

  print(f"El valor en la función padre antes es: {valor}")
  funcion_anidada()
  print(f"El valor en la función padre después es: {valor}")

funcion_padre()

# Importar variable local de otro modulo
from modulo import saludo

print(saludo)