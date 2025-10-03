class Shape:
   def __init__(self):
       pass
   def area(self):
       print("Area: 0")
class Square(Shape):
   def __init__(self, length):
       self.length = length
   def area(self):
       square_area = self.length * self.length
       print(f"Area of Square (side={self.length}): {square_area}")
print()
shape = Shape()
print("Shape area:")
shape.area()
length_input=float(input("enter number"))
square = Square(length_input)
print("Square area:")
square.area()