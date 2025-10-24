import re
s = input()
print("Match" if re.fullmatch(r'a{2,3}b{2,3}', s) else "No match")
