# Importar la biblioteca entera
import random

print(random.randrange(10))

# Importar únicamente una función
from random import randrange

print(randrange(10))

# Importar varias funciones
from random import randrange, choice

print(randrange(10))
print(choice(["uno", "dos", "tres"]))