def display(*args):
    for i in args:
        print(i)
display(3, 4, 5, 6)

def prod(*args):
    s = args[0]
    for i in args[1:]:
        s*=i
    print(s)
print(prod(2,8,4))

