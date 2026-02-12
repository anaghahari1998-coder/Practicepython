#number of parameters can be varied using variable length
# keyword--- *args

def sum(*args):
    s=0
    for i in args:
        s+=i
    return s
print(sum(2,3,5))

def sub(*args):
    s = args[0]
    for i in args[1:]:
        s-=i
    print(s)
print(sub(10,6,2))


