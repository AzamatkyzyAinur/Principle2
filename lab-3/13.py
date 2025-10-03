def has_33(nums):
   for i in range(len(nums) - 1):
       if nums[i] == 3 and nums[i+1] == 3:
           return True
   return False
nums = list(map(int, input("Enter numbers separated by space: ").split()))
result = has_33(nums)
print("\n--- Check for Consecutive Threes ---")
print(f"List: {nums}")
print(f"Has consecutive 3s? {result}")