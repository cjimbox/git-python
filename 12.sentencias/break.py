# Rompe un ciclo
numero = 5

while (numero < 10):
  numero += 1
  if numero == 8:
    break
  print(numero)
print("")

# Con un ciclo for
nums = [1,2,3,4,5]

for num in nums:
  print(num)
  if (num == 3):
    break