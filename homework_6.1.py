import time

class TrafficLight:
  __color = 'red'
    
  def running(self):
    while True:
      TrafficLight.__color = ('red')
      print(TrafficLight.__color)
      time.sleep(7)
      
      TrafficLight.__color = ('yellow')
      print(TrafficLight.__color)
      time.sleep(2)
      
      TrafficLight.__color = ('green')
      time.sleep(5)
      print(TrafficLight.__color)


traffic_light = TrafficLight()

traffic_light.running()