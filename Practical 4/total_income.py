months = int(input("How many months? "))
incomes = []
for month in range(1, months+1):
    income = float(input("Enter income for month " +str(month)+": "))
    incomes.append(income)
total = 0.0
print("Income Report\n-------------")

for month in range(1, months+1):
    income = incomes[month-1]
    total += income
    print("Month {:2} - Income: ${:5}Total: ${:10}".format(i, incomes[i], total))

