def main():
    password = input("Create your password: ")
    if strength(password):
        print ("Valid password")
def strength(s):
    a = 0
    b = 0
    c = 0
    d = 0
    for i in s:
        if i.isupper():
            a+=1
        elif i.islower():
            b+=1
        elif i.isdigit():
            c+=1
        elif not i.isalnum():
            d+=1
    if not a>=1:
        print("Your password must have at least one uppercase")
        return False
    elif not b>=1:
        print("Your password must have at least one lowercase")
        return False
    elif not c>=1:
        print("Your password must include at least one number")
        return False
    elif not d>=1:
        print("Your password must include at least one special character")
        return False
# Must have at least one uppercase, one lowercase, one number, and one special character#
    if not len(s)>=8:
        print("Minimum length of your password must be 8 characters")
        return False
    # Minimum length: 8 characters.
    if len(s) == 0:
        print("Password cannot be empty")
        return False
    return True
#Output messages showing *which rule failed* (to practice logical order).
main()
