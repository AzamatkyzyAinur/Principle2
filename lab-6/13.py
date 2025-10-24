import os

path = input("path do delete ")

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print("file deleted")
    else:
        print("access zhok")
else:
    print("file netu")
