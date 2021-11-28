string_arr = input().split()
for string in string_arr:
  index = string_arr.index(string) + 1
  if len(string) > 10:
    string = string[:10]
    print(f'{index}. {string}')
  else:
    print(print(f'{index}. {string}'))