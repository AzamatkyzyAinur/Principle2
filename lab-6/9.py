filename = input("file name")

with open(filename, 'r') as f:
    lines = f.readlines()
    print("number of lines in the file or text", len(lines))
