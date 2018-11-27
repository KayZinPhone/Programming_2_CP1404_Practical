"""
text_file = open("name.txt","w")
name = input("Enter your name: ")
print("Your name is ", name)
print("Your name is ", name, file=text_file)
"""

"""
output_file = open("name.txt", "r")
str =  output_file.readline();
print(str)
"""

"""
text_file = open("numbers.txt", "r")
num1 = int(text_file.readline())
num2 = int(text_file.readline())
print("num1: ",num1, "num2: ",num2)
result = num1 + num2
print("result: ",result)
text_file.close()
"""

text_file = open("numbers.txt", "r")
numlist = text_file.readlines()
total = 0
for i in numlist:
    new_num = int(i)
    total += new_num

print("result: ", total)
text_file.close()





