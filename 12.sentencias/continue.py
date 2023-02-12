# Cuando la condición se cumpla, pasas a la siguiente ejecución
nums = [1,2,3,4,5]

for num in nums:
  if num == 3:
    continue
  print(num)
print("")

# Con una cadena
nombre = "Jimmy"

for letra in nombre:
  if letra == 'm':
    continue
  print(letra)