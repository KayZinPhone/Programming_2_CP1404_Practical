print("Welcome to shop calculator")
no_item = int(input("Number of items: "))
total_amt = 0
for i in range(1, no_item+1, 1):
    item_price = float(input("Price of item: "))
    total_amt += item_price

if total_amt > 100:
    # total_amt = 0.9*total_amt
    total_amt = total_amt - (total_amt*0.10)
    print("Total price for ", no_item, " items is ", total_amt)
else:
    print("Total price for ", no_item, " items is ", total_amt)



