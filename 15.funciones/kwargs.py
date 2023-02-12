# Nombre por convención
def func(**kwargs):
  print(kwargs) # Diccionario
  print(*kwargs)
  if "fruit" in kwargs:
    print("Mi fruta escogida es: {}".format(kwargs["fruit"]))
  else:
    print("No hay fruta")

func(fruit="Manzana", veggie="Zanahoria")

# Puede ser cualquier nombre
def func(**fruit_veggies):
  print(fruit_veggies) # Diccionario
  print(*fruit_veggies)
  if "fruit" in fruit_veggies:
    print("Mi fruta escogida es: {}".format(fruit_veggies["fruit"]))
  else:
    print("No hay fruta")

func(fruit="Manzana", veggie="Zanahoria")