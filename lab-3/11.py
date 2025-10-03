from itertools import permutations
def print_permutations(s):
   perm_list = list(permutations(s))
   print(f"\n--- String Permutations for '{s}' ---")
   for p in perm_list:
       print("".join(p))
   print(f"Total unique permutations: {len(perm_list)}")
input_string = input("Enter a string: ")
print_permutations(input_string)