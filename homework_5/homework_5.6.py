with open('data_5.6.txt', 'r', encoding='utf-8') as f:
  data = f.readlines()

output = {}

for i, el in enumerate(data):
  
  subject = el.split(':').pop(0)
  value = 0
  
  for num in el.split():
    
    test_value = [str(i) for i in num if i.isdigit()]
    
    if test_value:
      value += int(''.join(test_value))
      
  output.update({subject: value})


print(output)