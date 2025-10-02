from turtle import Shape


class Rectangle(Shape):
   def __init__(self, length, width):
       # Initialize with length and width
       self.length = length
       self.width = width
   def area(self):
       # Area of a rectangle is length * width
       rectangle_area = self.length * self.width
       print(f"Area of Rectangle (l={self.length}, w={self.width}): {rectangle_area}")
print("\n")
rectangle = Rectangle(6, 4)
print("Rectangle area:")
rectangle.area()
# Inherits the default area from Shape if needed, but not common for a defined shape
# shape_rect = Shape()
# shape_rect.area()