n = int(input('Введите количество элементов массива: '))
arr = []
for i in range(n):
  arr.append(input())
print('Начальный', arr)
for i in range(0, n, 2):
  try:
    arr[i], arr[i + 1] = arr[i + 1], arr[i]
  except:
    break
print('Полученный', arr)