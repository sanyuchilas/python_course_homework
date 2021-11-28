proceeds = int(input('Введите значение выручки: '))
expenses = int(input('Введите значение издержек: '))
if proceeds >= expenses:
  profit = proceeds - expenses
  print('Прибыль: ', profit, sep = '')
  print('Рентабельность выручки: ', (profit / proceeds), sep = '')
  number = int(input('Введите количество сотрудников: '))
  print('Прибыль в расчёте на одного сотрудника: ', profit / number, sep = '')
else:
  loss = expenses - proceeds
  print('Убыток: ', loss, sep = '')