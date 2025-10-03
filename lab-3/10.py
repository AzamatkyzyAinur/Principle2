def is_prime(n):
   if n <= 1:
       return False
   for i in range(2, int(n**0.5) + 1):
       if n % i == 0:
           return False
   return True
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
prime_list = [n for n in numbers if is_prime(n)]
print("\n--- Prime Number Filter ---")
print("Original list:", numbers)
print("Prime numbers:", prime_list)