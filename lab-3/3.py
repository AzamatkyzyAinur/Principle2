from turtle import Shape
class Rectangle(Shape):
   def __init__(self, length, width):
       self.length = length
       self.width = width
   def area(self):
       rectangle_area = self.length * self.width
       print(f"Area of Rectangle (l={self.length}, w={self.width}): {rectangle_area}")
print("\n")
length_input=float(input("enter number: "))
width_input=float(input("enter number: "))
rectangle = Rectangle(length_input,width_input)
print("Rectangle area:")
rectangle.area()
