from statistics import mean
with open('data_5.3.txt', 'r') as f:
  data = f.read().split('\n')

avg = []
print('Оклад меньше 20 тыс. у работников:')  
for i, el in enumerate(data):
  avg.append(int(el.split().pop()))
  if int(el.split().pop()) < 20_000:
    print(el.split().pop(0)[:-1])
print(f'Средний доход сотрудников: {mean(avg)}')