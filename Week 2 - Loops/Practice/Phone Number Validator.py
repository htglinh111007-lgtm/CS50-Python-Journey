# Input: a string.
def main():
    phone_number = input("Phone number: ")
    if valid(phone_number):
        print("Valid phone number")
def valid(s):
    if not s[0] == "0":
        print ( "Phone number must start with 0 ")  # Must start with “0”
        return False
    if len(s)!=10:
        print("Phone number must contain exactly 10 digits")  # contain exactly 10 digits.
        return False
    if not s.isdigit():
        print("No letters allowed")  # no letters allowed            
        return False
    for i in s:
        if i == " ":
            print("No spaces allowed") # No spaces allowed.
            return False
    return True
main()



