river = "Mississippi"
target = input('Input a character to find: ')
fro index, letter in enumerate(river): #for index in range(len(river))
    if letter == target:
        print('Letter found at index ', index)
        break
else:
    print('Letter', target,'not found in ',river)



temp_file = open("temp.text", "r")