import re
s = input()
print("Match" if re.fullmatch(r'ab*', s) else "No match")
