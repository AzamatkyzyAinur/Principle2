import math
class Point:
   def __init__(self, x, y):
       # Initialize the coordinates
       self.x = x
       self.y = y
   def show(self):
       # Display the coordinates
       print(f"Point coordinates: ({self.x}, {self.y})")
   def move(self, new_x, new_y):
       # Change the coordinates
       self.x = new_x
       self.y = new_y
       print(f"Point moved to: ({self.x}, {self.y})")
   def dist(self, other_point):
       # Compute the distance to another Point object
       dx = self.x - other_point.x
       dy = self.y - other_point.y
       distance = math.sqrt(dx**2 + dy**2)
       return distance
print("\n")
p1 = Point(3, 4)
p2 = Point(0, 0)
print("Initial p1:")
p1.show()
print("Initial p2:")
p2.show()
p1.move(10, 5)
distance = p1.dist(p2)
print(f"Distance between p1({p1.x}, {p1.y}) and p2({p2.x}, {p2.y}): {distance:.2f}")