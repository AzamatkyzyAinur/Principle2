import os

path = input("Enter the path: ")

print("Directories:")
print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

print("files")
print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

print("all eements")
print(os.listdir(path))
