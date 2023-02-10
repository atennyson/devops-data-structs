"""Count words in file."""


# put your code here.
words_dict = {}

with open("test.txt") as file:
    lines = file.read().splitlines()
    for line in lines:
        words = line.split(" ")

        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

    print(words_dict)
