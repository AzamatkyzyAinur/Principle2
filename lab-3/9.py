def solve(numheads, numlegs):
   """
   Calculates the number of chickens and rabbits given the total heads and legs.
   Returns a tuple (chickens, rabbits) or (None, None) if no valid solution.
   """
   # Rabbits have 4 legs, chickens have 2. All have 1 head.
   # Check for invalid scenarios
   if numlegs < 2 * numheads or numlegs % 2 != 0 or numlegs > 4 * numheads:
       print("No valid solution exists for these numbers.")
       return (None, None)
   # Calculate number of rabbits (R)
   # R = (numlegs - 2 * numheads) / 2
   rabbits = (numlegs - 2 * numheads) // 2
   # Calculate number of chickens (C)
   # C = numheads - R
   chickens = numheads - rabbits
   return (chickens, rabbits)
# Example Usage:
numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print(f"\n--- Chickens and Rabbits Puzzle ---")
if result[0] is not None:
   print(f"Total Heads: {numheads}, Total Legs: {numlegs}")
   print(f"Chickens: {result[0]}")
   print(f"Rabbits: {result[1]}")
   # Verification: {result[0] + result[1]} heads, {2*result[0] + 4*result[1]} legs
else:
   print("Could not determine the number of animals.")