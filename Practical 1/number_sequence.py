x = int(input("Input X value: "))
y = int(input("Input Y value: "))


for i in range(x, y+1, 1):
    print(i, end=" ")
print("\n")

#1. Show the even numbers from x to y
for i in range(x, y + 1, 1):
    if (i % 2 == 0):
        print(i, end=" ")
print("\n")

#2. Show the odd numbers from x to y
for i in range(x, y+1, 1):
    if(i % 2 != 0):
        print(i, end=" ")
print("\n")


#3. Show the squares from x to y
for i in range(x, y+1, 1):
    print(i**2, end=" ")





