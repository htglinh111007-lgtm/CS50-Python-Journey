amount_due = 50
print ("Amount due: ", amount_due)
while amount_due > 0 :
    insert_coin = int(input("Insert coin: "))
    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        amount_due = amount_due - insert_coin
        if amount_due > 0:
             print ("Amount due: ", amount_due)
    else:
        amount_due = amount_due + 0
        print ("Amount due: ", amount_due)
print ("Change owed:", amount_due*(-1))
