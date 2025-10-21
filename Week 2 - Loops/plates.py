def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print ("Valid")
    else:
        print ("Invalid")
def is_valid(s):
    #contains maximum of 6 chars and minimum of 2chars#
    if not (len(s)<=6 and len(s)>=2):
        return False
    #start with 2 letters#
    if not(s[0].isalpha() and s[1].isalpha()):
        return False
     #no special characters#
    for i in s:
        if not i.isalnum():
            return False
    #first number exists <=> the last ones must be numbers#
    for i, char in enumerate(s):
        if char.isdigit():
                #first number != 0#
            if char == "0":
                return False
            if not s[i:].isdigit():
                return False
            break
    return True
main()


    
