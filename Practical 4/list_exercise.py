numbers = []
for i in range(1,6):
    number = int(input("Number: "))
    numbers.append(number)
print("The first number is ", numbers[0])
print("The last number is ", numbers[4])
print("The smallest number is ", min(numbers))
print("The largest number is ", max(numbers))
print("The average of the number is ", sum(numbers)/5)
