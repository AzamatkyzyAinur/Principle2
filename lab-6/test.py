import os
path= input()
if os.path.exists(path):
    directory, filename=os.path.split(path)
    name,ext =os.path.splitext(filename)
    print("Directorate",directory)
    print("File name", name)
    print("Extension", ext)
else:
    print("false")