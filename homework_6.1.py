import time

class TrafficLight:
  color = 'red'
    
  def running(self):
    while True:
      self.color = ('red')
      print(self.color)
      time.sleep(7)
      
      self.color = ('yellow')
      print(self.color)
      time.sleep(2)
      
      self.color = ('green')
      time.sleep(5)
      print(self.color)


traffic_light = TrafficLight()

traffic_light.running()