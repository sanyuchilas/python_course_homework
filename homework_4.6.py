from itertools import cycle
from itertools import count

start, end = map(int, input('Введите через пробел два числа - диапазон для генерации целых чисел: ').split())
cycler = cycle(range(start, end + 1))
for i in cycler:
  print(i)
  if i == end:
    break

print(f"\n{'-' * 30}\n") 
arr = [12, 2, 123, 34]
cycler_arr = cycle(arr)
for index, el in enumerate(cycler_arr):
  print(el)
  if el == arr[-1] and index == len(arr) - 1:
    break