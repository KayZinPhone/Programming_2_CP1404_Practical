count = 0
total = 0
average = 0
age = int(input("Enter age: "))
while age >= 0:

    count = count+1
    total += age
    average = total / count

    age = int(input("Enter age: "))



print("Total: ", total)
print("Average: ", average)

