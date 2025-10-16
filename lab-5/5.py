import re
s = input()
print("Match" if re.fullmatch(r'a.*b', s) else "No match")
