x = int(input("number:"))
print(x)

if x%2==0:
    print("even")
else:
    print("odd")

y = int(input("First number:"))
print(y)
z = int(input("Second number:"))
print(z)
w = input("choose arithmetic operation(+,-,*,/):")
if w == "+":
    print(y+z)
elif w == "-":
    print(y-z)
elif w == "*":
    print(y*z)
else:
    print(y/z)


