print("Electricity bill estimator")

price = float(input("Enter cents pre kWh:" ))
usage = float(input("Enter daily use in kWh: "))
days = int(input("Enter number of billing days: "))

estimated_bill = days * usage * (price/100)
print("Estimated bill: ", estimated_bill)


print("Electricity bill estimator 2.0")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

choice= int(input("Which tariff? 11 or 31: "))
usage = float(input("Enter daily use in kWh: "))
days = int(input("Enter number of billing days: "))

if choice == 11:
    estimated_bill = days * usage * TARIFF_11
    print("Estimated bill: ", estimated_bill)

elif choice == 31:
    estimated_bill = days * usage * TARIFF_11
    print("Estimated bill: ", estimated_bill)