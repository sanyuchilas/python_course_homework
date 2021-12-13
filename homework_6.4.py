class Car:
  def __init__(self, speed, color, name, is_police):
    self.speed = speed
    self.color = color
    self.name = name
    self.is_police = is_police
    
  def go(self, speed):
    print('Машина поехала')
    self.speed = speed
  
  def stop(self):
    print('Машина остановилась')
    self.speed = 0
    
  def turn(self, direction):
    print(f'Машина повернула {direction}')
  
  def show_speed(self):
    print(f'Ваша скорость - {self.speed} км/ч')
    
class TownCar(Car):
  def show_speed(self):
    print(f'Вы привышате скорость на {self.speed - 60} км/ч') if self.speed > 60 else print(f'Ваша скорость - {self.speed} км/ч')

class SportCar(Car):
  pass

class WorkCar(Car):
  def show_speed(self):
    print(f'Вы привышате скорость на {self.speed - 40} км/ч') if self.speed > 40 else print(f'Ваша скорость - {self.speed} км/ч')

class PoliceCar(Car):
  pass


towncar = TownCar(100, 'blue', 'жигуль', False)
sportcar = SportCar(100, 'blue', 'жигуль', False)
workcar = WorkCar(100, 'blue', 'жигуль', False)
policecar = PoliceCar(100, 'blue', 'жигуль', True)

policecar.show_speed()
policecar.stop()
policecar.show_speed()
policecar.go(100)
policecar.show_speed()

towncar.show_speed()
workcar.show_speed()