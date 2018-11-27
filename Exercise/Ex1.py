agelist = []
age = 0
total = 0
average = 0
age = int(input("Enter your age: "))
while age >= 0:

    agelist.append(age)

    for i in range(0, len(agelist)):
        total += agelist[i]

    average = total/len(agelist)
    age = int(input("Enter your age: "))

print("Total = ", total)
print("Average = ", average)







