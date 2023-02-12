# Todos los tipos de datos son instancias de sus clases
print(object); print(str); print(int); print(bool); print(tuple)
print(list); print(dict); print(set); print(float)

# Cada clase de cada tipo de dato, trae un método que nos permite convertir un dato a ese tipo de dato
a = "Hola"; b = 900; c = [9,2,3,4]; d = "1000"; e = "True"; f = "10.23"
g = [{"hola": "saludo", "adios": "despedida"}]

print(str(b)); print(int(d)); print(bool(e)); print(tuple(a))
print(list(c)); print(dict(g)); print(set(c)); print(float(f))