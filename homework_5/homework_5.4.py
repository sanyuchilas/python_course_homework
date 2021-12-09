num2words1 = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
with open('data_5.4.txt', 'r') as f:
  lines = f.readlines()
  for i, line in enumerate(lines):
    line = line.strip().split()
    line[0] = num2words1[int(line[-1])]
    lines[i] = ' '.join(line)
    
with open('new_data_5.4.txt', 'w', encoding='utf-8') as f_new:
  f_new.write('\n'.join(lines))