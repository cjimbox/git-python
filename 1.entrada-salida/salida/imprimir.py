# sys.stdout == print()

# Imprimir una cadena
print("Hola Mundo")

# Imprimir más de un objeto (parámetro objects*)
print("hola", "adiós")

# Imprimir con separador (parámetro sep)
print("Hola", "Amigos", sep="     ")

# Imprimir algo al final (parámetro end)
edad = 11
print("Hola", "Kevin", "tienes", edad, "años", sep="  ", end="\n\n")
print("Jaja")

# Cambiar la salida de ejecución (parámetro file)
sourceFile = open("nueva-salida.txt", "w")
print("Hola Random", end="\n\n", file=sourceFile)
print("Hola esto es un texto", file=sourceFile)
  # Si no hubiera una variable que habrà el archivo usarìa esta salida
print("Hola esto es un texto", file=open("nueva-salida.txt", "w"))
sourceFile.close()

# Vaciar la salida
salida = print("Esto se vaciarà", flush=True)
print(salida) # = None

# Combinar operaciones
nombre = "Alicia"
edad = 35

print("Hola", "soy", nombre, "tengo", 35, "años")

# Hacer una suma
print(8 + 12)

# Sumar flotantes
a = 12.9
b = 90.5
print(a + b)

# Imprimir el valor de una variable
nombre = "Jimmy"
print(f"{nombre = }")

