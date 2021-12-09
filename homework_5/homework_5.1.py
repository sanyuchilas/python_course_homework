with open('data_5.1.txt', 'a') as f:
  while True:
    input_data = input('Введите данные: ')
    if input_data:
      f.write(input_data)
    else:
      break
    f.write('\n')