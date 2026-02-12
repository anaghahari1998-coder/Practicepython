def exception(x,y):
    try:
        if y == 0:
            raise ZeroDivisionError("Numbers cannot be divided by zero")
    except ZeroDivisionError as e:
        print(e)
    else:
        print("else block is executed")
    finally:
        print("Action is executed")
    return x/y
exception(6,3)
exception(7,0)   #exceptional error
print(exception(4,2))
