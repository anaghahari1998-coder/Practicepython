# for i in range(1,6,1):
#     print(i)
# for i in range(5):
#     print(i)
# for i in range(1,6,2):
#     print(i)
# name = "Anagha"
# for i in name:
#     print(name)
# size = len(name)
# print(size)
# for i in range(size):
#     print(name[i])
# name = "anjali"
# i = 0
# count = 0
# while i<len(name):
#     if (name[i] == 'a' or
#            name[i] == 'e' or
#             name[i] == 'i' or
#             name[i] == 'o' or
#             name[i] == 'u'):
#         count = count+1
#         print(name[i])
#     i = i+1
# print(count)
name = "anjali"
i = 0
count = 0
while i<len(name):
    if (name[i] == 'a' or
           name[i] == 'e' or
            name[i] == 'i' or
            name[i] == 'o' or
            name[i] == 'u'):
        count = count+1
        print(name[i])
    i = i+1
else:
    print("Condition is not met")
print(count)
