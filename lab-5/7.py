s = input()
parts = s.split('_')
print(parts[0] + ''.join(word.title() for word in parts[1:]))
