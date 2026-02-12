# set1={}
# print(set1)
# list1=[10,20,30,30]
# set2=set(list1)
# print(set2)
#
# set2.remove(10)
# print(set2)

setA={20,40,45,67}
setB={20,40,45,67,98}
# setA.difference_update(setB)
# print(setA)
# setB.difference_update(setA)
# print(setB)
print(setA.issubset(setB))
print(setB.issubset(setA))
print(setA.issuperset(setB))
print(setB.issuperset(setA))