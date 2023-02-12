# Reasignación de variables
x = 50

def func():
  global x
  print(f"x es: {x}")

  x = "Nuevo valor"
  print(f"Fue localmente cambiada de {x} a: {x}")

func()
print(x)