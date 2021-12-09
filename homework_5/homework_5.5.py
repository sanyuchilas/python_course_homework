num_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
num_tuple = tuple(map(str, num_tuple))
with open('data_5.5.txt', 'w') as f:
  f.write('\n'.join(num_tuple))

with open('data_5.5.txt', 'r') as f:
  new_num_tuple = tuple(map(float, f.readlines()))
print(new_num_tuple)
print(sum(new_num_tuple))