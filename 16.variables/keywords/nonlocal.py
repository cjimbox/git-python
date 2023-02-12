# Keyword nonlobal
def funcion_padre():
  valor = 10

  def funcion_anidada():
    nonlocal valor
    valor = 20
    print(f"El valor en la función anidada es: {valor}")

  print(f"El valor en la función padre antes es: {valor}")
  funcion_anidada()
  print(f"El valor en la función padre después es: {valor}")

funcion_padre()