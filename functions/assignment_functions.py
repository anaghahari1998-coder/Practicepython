def square(x):
    return x*x
print(square(3))

def number(y):
    if y%2==0:
        print("Number is even")
check_number=int(input("Enter a number:"))
number(check_number)

def text(word):
    return len(word)
msg = input("Enter a word:")
print(text(msg))

def newword(name):
    return name[0]
text2 = input("Enter a new word:")
print(newword(text2))
