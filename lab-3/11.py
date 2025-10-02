from itertools import permutations
def print_permutations(s):
   """Accepts a string and prints all its unique permutations."""
   # Get all permutations as tuples of characters
   perm_list = list(permutations(s))
   print(f"\n--- String Permutations for '{s}' ---")
   # Convert tuples back to strings and print
   for p in perm_list:
       print("".join(p))
   print(f"Total unique permutations: {len(perm_list)}")
# Example Usage:
input_string = "cat"
print_permutations(input_string)