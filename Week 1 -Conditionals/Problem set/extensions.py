file = input("File name: ")
if file.endswith(".gif"):
    print ("image/gif")
elif file.endswith(".jpeg"):
    print ("image/jpeg")
else:
    print("application/octet-strem")

