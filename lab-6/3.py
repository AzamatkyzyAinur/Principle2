s = input("line")
s_clean = s.lower().replace(" ", "")

if s_clean == s_clean[::-1]:
    print("it is palindrome")
else:
    print("it is not palindrome")
