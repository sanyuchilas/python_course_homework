from math import factorial
def fact(n):
  def gener():
    for i in range(1, n + 1):
      yield factorial(i)
  return gener()
for el in fact(4):
  print(el)