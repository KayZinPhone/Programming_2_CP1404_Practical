import random

UPPER_CHAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_CHAR = "abcdefghijklmnopqrstuvwxyz"
SPECIAL_CHAR = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


pwd_length = int(input("Enter the length of password: "))
upper_char_count = int(input("Enter the length of upper character: "))
lower_char_count = int(input("Enter the length of lower character: "))
special_char_count = int(input("Enter the length of special character: "))
digit_count = int(input("Enter the length of digit: "))

if pwd_length != upper_char_count + lower_char_count + special_char_count + digit_count:
    print("The length should be equal to password length")
    pwd_length = int(input("Enter the length of password: "))
    upper_char_count = int(input("Enter the length of upper character: "))
    lower_char_count = int(input("Enter the length of lower character: "))
    special_char_count = int(input("Enter the length of special character: "))
    digit_count = int(input("Enter the length of digit: "))
else:
    word = ""
    """
    for kind in range(1, 5):
        if kind == 1:
            word += random.choice(UPPER_CHAR)
            upper_char_count -= 1
        elif kind == 2:
            word += random.choice(LOWER_CHAR)
            lower_char_count -= 1
        elif kind == 3:
            word += random.choice(SPECIAL_CHAR)
            special_char_count -= 1
        elif kind == 4:
            word += str(random.randint(1, 9))
            digit_count -= 1
   """

    for i in range(1, 1000):
        generator = random.randint(1, 5)
        if generator == 1:
            while upper_char_count != 0:
                word += random.choice(UPPER_CHAR)
                upper_char_count -= 1
                print("{:<}{:>20}{:10}".format(generator, word, upper_char_count))
        elif generator == 2:
            while lower_char_count != 0:
                word += random.choice(LOWER_CHAR)
                lower_char_count -= 1
                print("{:<}{:>20}{:10}".format(generator, word, lower_char_count))
        elif generator == 3:
            while special_char_count != 0:
                word += random.choice(SPECIAL_CHAR)
                special_char_count -= 1
                print("{:<}{:>20}{:10}".format(generator, word, special_char_count))
        elif generator == 4:
            while digit_count != 0:
                word += str(random.randint(1, 9))
                digit_count -= 1
                print("{:<}{:>20}{:10}".format(generator, word, digit_count))

"""
while upper_char_count != 0 and lower_char_count != 0 and special_char_count != 0 and digit_count != 0:
    
    word += random.choice(UPPER_CHAR)
    upper_char_count -= 1
    print("{}{:2}".format(word, upper_char_count))

    word += random.choice(LOWER_CHAR)
    lower_char_count -= 1
    print("{}{:2}".format(word, lower_char_count))

    word += random.choice(SPECIAL_CHAR)
    special_char_count -= 1
    print("{}{:2}".format(word, special_char_count))

    word += str(random.randint(1, 9))
    digit_count -= 1
    print("{}{:2}".format(word, digit_count))"""

if upper_char_count == 0 and lower_char_count == 0 and special_char_count == 0 and digit_count == 0:
        print(word)