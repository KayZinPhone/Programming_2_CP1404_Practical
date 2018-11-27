import string

str = input("Enter a string: ")

def count(str):
    """Return the number of letters in text."""
    count = 0
    for character in str:
        if character.lower() in string.ascii_letters:
            count+=1
    return count

print(count(str))