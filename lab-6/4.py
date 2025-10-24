import time
import math

num = int(input("number "))
milliseconds = int(input("milli secondd "))

time.sleep(milliseconds / 1000)
result = math.sqrt(num)

print(f"The square root of {num} after {milliseconds} milliseconds is {result}")
