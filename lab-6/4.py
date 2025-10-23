import time
import math

num = int(input("number "))
milliseconds = int(input("milli secund "))

time.sleep(milliseconds / 1000)
result = math.sqrt(num)

print(f"The square root of {num} after {milliseconds} milliseconds is {result}")
