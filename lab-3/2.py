class Shape:
   def __init__(self):
       pass
   def area(self):
       # Default area is 0 for a generic shape
       print("Area: 0")
class Square(Shape):
   def __init__(self, length):
       # Initialize with the length (side)
       self.length = length
   def area(self):
       # Area of a square is length * length
       square_area = self.length * self.length
       print(f"Area of Square (side={self.length}): {square_area}")
print()
shape = Shape()
print("Shape area:")
shape.area()
square = Square(5)
print("Square area:")
square.area()