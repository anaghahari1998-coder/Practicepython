for i in range(1,11):
    if i%2==1:
     print(i)

text = " "
while text != "exit":
    text=input("Enter the text . please enter exit to stop entering:")
    print(text)
    if text == "exit":
        print("Loop is closed")
