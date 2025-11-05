def main():
    price = price_to_float(input("Enter the product price: "))
    discount = discount_to_float(input("Enter discount: "))
    bill = price - (price*discount)
    print (f"You need to pay {bill:.2f}")
def price_to_float (p):
    return float(p.replace("đ",""))
def discount_to_float (d):
    return float(d.replace("%",""))/100
main()