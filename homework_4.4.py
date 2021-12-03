arr_input = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
arr_repeat = []

def gener():
  for i in range(len(arr_input)):
    for k in range(i + 1, len(arr_input)):
      if arr_input[i] == arr_input[k]:
        for el in arr_repeat:
          if el == arr_input[i]:
            break
        else:
          arr_repeat.append(arr_input[i])
          yield arr_input[i]
          
arr_repeat = list(gener())
arr_output = []

for el in arr_input:
  for repeat in arr_repeat:
    if el == repeat:
      break
  else:
    arr_output.append(el)
      
print(arr_output)