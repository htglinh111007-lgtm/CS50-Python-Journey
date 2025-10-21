greet = input ("Greeting: ")
if greet.lower().startswith("hello"):
    print ("$0")
elif greet.lower().startswith("h") and greet.lower() != "hello":
    print ("$20")
else:
    print ("$100")

