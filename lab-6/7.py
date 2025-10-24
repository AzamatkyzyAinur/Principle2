import os

path = input("the path: ")

print( os.access(path, os.F_OK))
print( os.access(path, os.R_OK))
print( os.access(path, os.W_OK))
print( os.access(path, os.X_OK))
