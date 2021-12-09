with open('data_5.2.txt', 'r') as f:
  data = f.read().split('\n')
  
print('Количество строк: ' + str(len(data)))

for i, el in enumerate (data):
  print(f"Количество слов в строке {i + 1}: {len(el.split())}")