import re
s = input()
print("Match" if re.findall(r's*' +'ing', s) else "No match")