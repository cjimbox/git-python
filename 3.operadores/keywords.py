# in - Devuelve True si un elemento se encuentra dentro de otro
d = {"k1":1}

if 1 in d.keys(): print("Verdadero") 
else: print("Falso")

if 1 in d.values(): print("Verdadero") 
else: print("Falso")

# not in - El operador Not in devuelve True si un elemento no se encuentra dentro de otro
if 1 not in d.keys(): print("Verdadero")
else: print("Falso")

if 1 not in d.values(): print("Verdadero")
else: print("Falso")

# is - Devuelve True si los elementos son exactamente iguales. Si ambas variables tienen el mismo valor son iguales
a = "a"
b = "b"

if a is b: print("Verdadero")
else: print("Falso")

# is not - Devuelve True si los elementos no son iguales. Si las variables tienen diferente valor son desiguales
if a is not b: print("Verdadero")
else: print("Falso")