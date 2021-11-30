print('1. Вводите все числа через пробел, прогрмамма будет выводить сумму всех когда-либо введеных чисел\n2. Для завершения программы введите вместо последнего числа q, для продолжения программы нажмите Enter')
def main():
  numbers_sum = 0
  
  def check_correct_input(number):
    if not(number.isdigit()):
      return number
    return float(number)
  
  while True:
    numbers = list(map(check_correct_input, input('Введите числа: ').split()))
    
    if numbers[-1] == 'q':
      numbers.pop(-1)
      print(numbers_sum + sum(numbers))
      break
    elif type(numbers[-1]) is 'string':
      print('Пожалуйста, введите число или q')
      continue
      
    numbers_sum += sum(numbers)
    print(numbers_sum)
  
main()