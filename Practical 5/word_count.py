text = input("Text: ").strip().split(" ")
word_to_count = {}
for word in text:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

for word in word_to_count:
    print("{:5s}: {}".format(word, word_to_count[word]))