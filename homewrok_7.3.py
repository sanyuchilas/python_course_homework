class Cell:
  def __init__(self, count):
    self.count = count
    
  
  def make_order(self, count_row):
    return ((self.count // count_row) * ('*' * count_row + '\n'))[:-1] if self.count % count_row == 0 else (self.count // count_row) * ('*' * count_row + '\n') + (self.count % count_row) * '*'
  
  
  def __add__(self, other):
    return Cell(self.count + other.count)
  
  
  def __sub__(self, other):
    return Cell(self.count - other.count) if self.count > other.count else 'Отрицательное количетсов клеток невозможно'
  
  
  def __mul__(self, other):
    return Cell(self.count * other.count)
  
  
  def __truediv__(self, other):
    return Cell(self.count // other.count)
  
  

cell1 = Cell(12)
cell2 = Cell(6)

print((cell1 + cell2).count)
print((cell1 - cell2).count)
print((cell2 - cell1))
print((cell1 * cell2).count)
print((cell1 / cell2).count)

print('---------')

print((cell1 * cell2).make_order(20))

print('---------')

print(cell1.make_order(5))
print('---------')
print(cell1.make_order(6))