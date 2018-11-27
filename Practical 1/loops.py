""""
Displays all of the odd numbers between 1 and 20 with a space between each one
"""
for i in range(1, 21, 2):
        print(i," ", end=' ')
print("\n")
"""
a.Count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100
"""
for i in range(0, 101, 10):
        print(i," ", end=" ")

print("\n")
"""
b.Count down from 20 10 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
"""
for i in range(20, 0, -1):
    print(i, " ", end=" ")

print("\n")
"""
c.Print n stars. ask the user for a number, then print that many star(*), all on one line
"""
num = int(input("Enter a number to display the number of star: "))
for i in range(0, num, 1):
    print('*', end='')

print("\n")
"""
d.Print n lines of increasing stars. 
*
**
***
****
"""

for i in range(1, 5, 1):
    for j in range(1, i+1, 1):
            print('*', end='')
    print(" ")

print("\n")