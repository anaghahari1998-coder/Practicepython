text = input("Name:")
print(text.lower())
print(text.upper())

word = input("Name:")
print(word.lower())
i = 0
count = 0
while i<len(word):
    if (word[i] == 'a' or
           word[i] == 'e' or
            word[i] == 'i' or
            word[i] == 'o' or
            word[i] == 'u'):
        count = count+1
        print(word[i])
    i = i+1

