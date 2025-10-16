import re

pattern = re.compile(r'\b[a-z]+(?:_[a-z]+)+\b')

def find_lowercase_underscore_sequences(text):
    return pattern.findall(text)

if __name__ == "__main__":
    s = input()
    matches = find_lowercase_underscore_sequences(s)
    if matches:
        print()
        for m in matches:
            print(m)
    else:
        print("no find")
