import random

count = int(input("How many quick picks?"))
for row in range(1,count+1):
    for col in range(1,7):
        num = random.randint(1,45)
        print("{:>}".format(num), end=" ")
    print("\n")