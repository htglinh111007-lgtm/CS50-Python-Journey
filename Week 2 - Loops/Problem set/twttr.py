a = input("Input: ")
for letter in a:
    if letter.lower() in "aeoui":
        a = a.replace(letter,"")
print("Output: ", a)