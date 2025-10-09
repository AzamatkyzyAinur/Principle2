import math

n = int(input("Input number of sides: "))

s = float(input("Input the length of a side: "))

angle_rad = math.pi / n

area_polygon = (n * s**2) / (4 * math.tan(angle_rad))

print(f"Input number of sides: {n}")

print(f"Input the length of a side: {s}")

print(f"The area of the polygon is: {area_polygon}")
 
