amount_due = 50
print ("Amount due: 50")
while amount_due > 0:
    insert_coin = int(input("Insert coin: "))
    if insert_coin == 25 or 10 or 5:
        amount_due = amount_due - insert_coin
        print ("Amount due: " , amount_due)
    else:
        print ("Amount due: ", amount_due)
print("Change owed: 0")
    
