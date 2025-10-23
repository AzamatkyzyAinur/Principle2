items = input("input ").split()
filename = input("file input  ")

with open(filename, 'w') as f:
    for item in items:
        f.write(f"{item}\n")

print("result")
