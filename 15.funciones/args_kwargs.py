# Podemos trabajar con los dos juntos
def func(*args, **kwargs):
  print(args); print(kwargs)
  print("Me gustaría {} {}s".format(args[1], kwargs["fruit"]))

func(10, 20, fruit="Manzana", veggie="Lechuga")