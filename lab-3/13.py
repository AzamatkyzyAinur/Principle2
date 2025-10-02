def has_33(nums):
   """
   Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
   """
   # We iterate up to len(nums) - 1 because we check i and i+1 in each loop
   for i in range(len(nums) - 1):
       # Check if the current element (nums[i]) and the next element (nums[i+1]) are both 3
       if nums[i] == 3 and nums[i+1] == 3:
           return True
   # If the loop completes without finding '3, 3', return False
   return False
# Example Usage:
print(f"\n--- Check for Consecutive Threes (has_33) ---")
print(f"has_33([1, 3, 3]) -> {has_33([1, 3, 3])}")       # Expected: True
print(f"has_33([1, 3, 1, 3]) -> {has_33([1, 3, 1, 3])}") # Expected: False
print(f"has_33([3, 1, 3]) -> {has_33([3, 1, 3])}")       # Expected: False
print(f"has_33([3, 3, 1, 5]) -> {has_33([3, 3, 1, 5])}") # Expected: True
print(f"has_33([5]) -> {has_33([5])}")                   # Expected: False