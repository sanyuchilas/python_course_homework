class Matrix:
  def __init__(self, arr):
    self.arr = arr
    
    
  def __str__(self):
    new_arr = []
    
    for i in self.arr:
      i = map(str, i)
      new_arr.append(' '.join(i))
      
    return '\n'.join(new_arr)
  
  
  def __add__(self, other):
    new_arr = []
    
    for i in range(len(self.arr) if len(self.arr) >= len(other.arr) else len(other.arr)):
      
      try:
        new_arr.append([' '.join(j) for j in zip(list(map(str, self.arr[i])), list(map(str, other.arr[i])))])
        
      except:
        new_arr.append((self.arr[i] if len(self.arr) >= len(other.arr) else other.arr[i]))
      
    new_matrix = Matrix(new_arr)
    
    return new_matrix


#Строки в матрицах должны быть одинаковой длины, но количество строк может отличаться

matrix1 = Matrix([[1, 2], [4, 5], [7, 8]])
matrix2 = Matrix([['hi', 'bye'], ['привет', 'пока']])

new_matrix = matrix1 + matrix2
print(str(new_matrix))