from functools import reduce

numbers = list(map(int, input("input").split()))
result = reduce(lambda x, y: x * y, numbers)
print("result", result)
