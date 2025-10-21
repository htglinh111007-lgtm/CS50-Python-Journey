def main():
    a = input()
    print(convert(a))
def convert (a):
    a = a.replace(":)", "🙂" ).replace(":("," 🙁" )
    return a
main()
