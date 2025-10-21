def main():
    email = input("Create your Email account: ")
    if valid(email):
        print("Your Email acount is valid")
def valid(s):
    a = 0
    for i in s:
        if i == "@":
            a+=1
        if a!=1:
                print(" Your Email account must contain exactly one "@" ")
                return False
        if i == " ":
            print("No spaces allowed")
    return True
main()
# Must contain exactly one “@”
# Must have at least one “.” after “@”.
# No spaces allowed