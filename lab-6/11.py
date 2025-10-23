import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", 'w') as f:
        f.write(f"Это файл {letter}.txt\n")

print("txt file created")
