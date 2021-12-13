class Road:
  length = 5000
  width = 20
  
  def __init__(self, mass, thickness):
    self.mass = mass
    self.thickness = thickness
    
  def calculate_road_mass(self):
    return self.length * self.width * self.mass * self.thickness


road = Road(25, 5)

print(f'{road.calculate_road_mass() // 1000} т')