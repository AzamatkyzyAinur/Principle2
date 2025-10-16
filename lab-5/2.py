import re
s = input()
print("Match" if re.fullmatch(r'ab{2,3}', s) else "No match")
