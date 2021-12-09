import json

with open('data_5.7.txt', 'r', encoding='utf-8') as f:
  data = f.readlines()

output_arr = []
avg = 0

for i, el in enumerate(data):
  
  firm = el.split().pop(0)
  profit = int(el.split().pop(2)) - int(el.split().pop(3)) 
  
  output_arr.append({firm: profit})
  avg += profit

output_arr.append({"average_profit": avg / (i + 1)})  

with open('homework_5/data_5.7.json', 'w', encoding='utf-8') as f:
  json.dump(output_arr, f)