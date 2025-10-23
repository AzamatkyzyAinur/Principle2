import shutil

src = input("Введите имя исходного файла: ")
dst = input("Введите имя файла назначения: ")

shutil.copyfile(src, dst)
print("ctrlv&ctrlc is final")
