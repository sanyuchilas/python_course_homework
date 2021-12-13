class Worker:
  name = 'Вася'
  surname = 'Булочкин'
  position = 'full-stack'
  _income = {'wage': 300_000, 'bonus': 50_000}
  
class Position(Worker):
  def get_full_name(self):
    return f'{self.name} {self.surname}'
    
  def get_total_income(self):
    return self._income['wage'] + self._income['bonus']
  
worker = Position()

print(f'Сотрудник {worker.get_full_name()} заработал {worker.get_total_income()} руб.')