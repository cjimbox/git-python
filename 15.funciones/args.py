# Nombre por convención
def suma(*args):
  print(args) # Tupla
  print(*args)
  print(args[1])
  print(sum(args) * 0.05)

suma(10,20,30)

# Puede ser cualquier nombre
def suma(*nums):
  print(*nums)
  print(nums[1])
  print(sum(nums) * 0.05)

suma(20,40,100)