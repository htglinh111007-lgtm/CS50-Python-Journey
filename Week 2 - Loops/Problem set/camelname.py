name = input("camelCase: ")
for i in name:
    if i.isupper():
       name = name.replace(i,"_"+i.lower())
print("snake_case: ", name)
