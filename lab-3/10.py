def is_prime(n):
   """Helper function to check if a single number is prime."""
   if n <= 1:
       return False
   for i in range(2, int(n**0.5) + 1):
       if n % i == 0:
           return False
   return True
def filter_prime(numbers):
   """Takes a list of numbers and returns only the prime numbers."""
   prime_numbers = [n for n in numbers if is_prime(n)]
   return prime_numbers
# Example Usage:
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15]
print(f"\n--- Prime Number Filter ---")
print(f"Original list: {number_list}")
prime_list = filter_prime(number_list)
print(f"Prime numbers: {prime_list}")