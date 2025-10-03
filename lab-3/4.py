import math
class Point:
   def __init__(self, x, y):
       self.x = x
       self.y = y
   def show(self):
       print(f"Point coordinates: ({self.x}, {self.y})")
   def move(self, new_x, new_y):
       self.x = new_x
       self.y = new_y 
       print(f"Point moved to: ({self.x}, {self.y})")
   def dist(self, other_point):
       dx = self.x - other_point.x
       dy = self.y - other_point.y
       distance = math.sqrt(dx**2 + dy**2)
       return distance
print("\n")
x1 = float(input("Enter x: "))
y1 = float(input("Enter:y"))
p1 = Point(x1,y1)
x2 = float(input("Enter x: "))
y2 = float(input("Enter:y"))
p2 = Point(x2,y2)
print("Initial p1:")
p1.show()
print("Initial p2:")
p2.show()
new_x1 = float(input("enter new x : "))
new_y1 = float(input("enter new y: "))
p1.move(new_x1,new_y1)
distance = p1.dist(p2)
print(f"Distance between p1({p1.x}, {p1.y}) and p2({p2.x}, {p2.y}): {distance:.2f}")