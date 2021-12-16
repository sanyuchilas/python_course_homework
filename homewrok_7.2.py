class Clothes:
  def __init__(self, name):
    self.name = name


class Coat(Clothes):
  def __init__(self, size, name):
    super().__init__(name)
    self.size = size

  def calculate(self):
    return f'{self.size / 6.7 + 0.5} ткани нужно для "{self.name}"'


class Costume(Clothes):
  def __init__(self, growth, name):
    super().__init__(name)
    self.growth = growth
    
  def calculate(self):
    return f'{self.growth * 2 + 0.3} ткани нужно для "{self.name}"'
  
  
coat = Coat(70, 'Зимнее пальто')
costume = Costume(120, 'Летний костюм')
  
print(coat.calculate())
print(costume.calculate())