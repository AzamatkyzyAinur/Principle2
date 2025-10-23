import os

path = input("Введите путь к файлу для удаления: ")

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print("file deleted")
    else:
        print("access zhok")
else:
    print("file netu")
