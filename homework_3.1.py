first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))

def division(a, b):
  if b != 0:
    print(a / b)
  else:
    print('Деление на 0 невозможно. Введите другое число')
division(first_num, second_num)