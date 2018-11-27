"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
"""
Add a loop to the sales bonus exercise, so that the program repeatedly asks for the user's sales and prints the bounus until they enter a negative number.
"""

sales = float(input("Enter sales: $"))
while sales > 0:
    if sales < 1000:
        bonus = sales*0.1
        print("sales: ", sales)
        print("bonus: ", bonus)

    elif sales >= 1000:
        bonus = sales*0.15
        print("sales: ", sales)
        print("bonus: ", bonus)
    sales = float(input("Enter sales: $"))








