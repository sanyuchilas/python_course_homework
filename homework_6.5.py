class Stationery:
  def __init__(self, title):
    self.title = title
    
  def draw(self):
    print('Запуск отрисовки')

class Pen(Stationery):
  def draw(self):
    print(f'Запуск отрисвоки "{self.title}" ручкой')

class Pencil(Stationery):
  def draw(self):
    print(f'Запуск отрисвоки "{self.title}" карандашом')

class Handle(Stationery):
  def draw(self):
    print(f'Запуск отрисвоки "{self.title}" маркером')
    
pen = Pen('смайлик')
pencil = Pencil('домик')
handle = Handle('кошка')

pen.draw()
pencil.draw()
handle.draw()