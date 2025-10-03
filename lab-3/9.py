def solve(numheads, numlegs):
   if numlegs < 2 * numheads or numlegs % 2 != 0 or numlegs > 4 * numheads:
       print("No valid solution exists for these numbers.")
       return (None, None)
   rabbits = (numlegs - 2 * numheads) // 2
   chickens = numheads - rabbits
   return (chickens, rabbits)
numheads = int(input("Enter total number of heads: "))
numlegs = int(input("Enter total number of legs: "))
result = solve(numheads, numlegs)
print("\n--- Chickens and Rabbits Puzzle ---")
if result[0] is not None:
   print(f"Total Heads: {numheads}, Total Legs: {numlegs}")
   print(f"Chickens: {result[0]}")
   print(f"Rabbits: {result[1]}")
else:
   print("Could not determine the number of animals.")