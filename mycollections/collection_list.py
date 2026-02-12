list1=["cat","dog","tiger"]
print(list1)
print(type(list1))
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[-1])

list2=[]
print(list2)
print(len(list1))
print(len(list2))

list1[1]="fish"      # to modify a list
print(list1)

list3=[20, "pink", "blue", 9]  # different datatypes can be added
print(list3)
print(list3.index("pink"))
list1.sort(reverse=True)
print(list1)
list1.sort()
print(list1)
list1.pop(0)
print(list1)