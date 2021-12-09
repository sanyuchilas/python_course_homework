def int_func(string):
  return string[0].upper() + string[1:]
# print(int_func('text'))
word_array = list(input('Введите слова через пробел: ').split())
for word in word_array:
  print(int_func(word), end=' ')