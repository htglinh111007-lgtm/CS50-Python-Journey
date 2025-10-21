def main():
    name = input("Create your username: ")
    if is_valid(name):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    #start with a letter#
    if not s[0].isalpha():
        return False
    #3<=len<=15#
    if not (len(s)>=3 and len(s)<=15):
        return False
    #only contains letters, digits and underscores#
    for i in s:
        if not (i.isalnum() or i == "_"):
            return False
    return True
main()