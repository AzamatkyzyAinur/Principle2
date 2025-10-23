import os

path = input("road input ")

if os.path.exists(path):
    print(" road bar")
    print("catalog", os.path.dirname(path))
    print("file name", os.path.basename(path))
else:
    print("zhol zhok")
