input_arr = list(map(float, input('Введите любое количество чисел через пробел: ').split()))

def gener():
  count = 0
  for i in range(len(input_arr) - 1):
    if input_arr[i + 1] > input_arr[i]:
      yield input_arr[i + 1]
    count += 1
output_arr = gener()
print(*output_arr)