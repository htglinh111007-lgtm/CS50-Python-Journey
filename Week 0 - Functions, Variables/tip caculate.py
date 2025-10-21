def main():
    bill =bill_to_float(input("How much was the bill? "))
    amount_of_tip =tip_to_float(input("How much would you like to tip? "))
    tip = bill*amount_of_tip
    print(f"Leave {tip:.2f} dollars,please!")
def bill_to_float(b):
    return float(b.replace("$",""))
def tip_to_float(t):
    return float(t.replace("%",""))/100
main()
