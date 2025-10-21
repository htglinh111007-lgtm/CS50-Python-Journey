def main():
    s = input ("Quãng đường bạn đi là: ")
    km = convert(s)
    if 0<km<=1:
        fee = 10000
        print(f"Your taxi fee is: {fee:.2f}")
    elif 2<=km<=5:
        fee = 10000 + (km-1)*8000
        print(f"Your taxi fee is: {fee:.2f}")
    elif km>5:
        fee = 42000 + (km-5)*6000
        print(f"Your taxi fee is: {fee:.2f}")
def convert(s):
    return float(s.replace("km", ""))

main()

