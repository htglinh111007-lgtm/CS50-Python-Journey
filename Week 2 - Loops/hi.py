s = input("Type: ")
for i, char in enumerate(s):
    if char.isdigit():
        if s[i:].isdigit():
            print("true")