text = input("input")

upper_count = sum(1 for c in text if c.isupper())
lower_count = sum(1 for c in text if c.islower())

print("capital letters", upper_count)
print("lowercase letters", lower_count)
