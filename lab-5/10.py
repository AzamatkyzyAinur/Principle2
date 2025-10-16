import re
s = input()
s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
print(re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower())
