def is_prime(n):
   """A helper function to check if a number is prime."""
   if n <= 1:
       return False
   # Check for factors from 2 up to the square root of n
   for i in range(2, int(n**0.5) + 1):
       if n % i == 0:
           return False
   return True
# Original list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17, 20]
# 1. Filtering using the is_prime function
# The filter() function applies the is_prime function to every item in 'numbers'.
prime_numbers = list(filter(is_prime, numbers))
# 2. Example of a simple filter using lambda (e.g., filter numbers greater than 5)
# large_numbers = list(filter(lambda x: x > 5, numbers))
print("\n")
print(f"Original list: {numbers}")
print(f"Prime numbers (using filter and a helper function): {prime_numbers}")