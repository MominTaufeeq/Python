'''List is change able .tuple is not chamge able.In list we can store any data type.
In list the index number start 0 '''
l=[5,7,4,"taufeeq",True]
# print(l)
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[4])
# print(l[-1])#-1 start from last element of list
# print(l[len(l)-3])
# # print(l[5-3])
# if "taufeeq" in l:
#     print("Yes")
# else:
#     print("No")
'''Same thing applied on string .'''
# if "tauf" in "taufeeq":
#     print("Yes")
# else:
#     print("No")
# marks=[5,6,9,"taufeeq",78,97,0,10,20,70,10]
# print(marks)
# print(marks[1:8])
# print(marks[1:8:2])# 2 is jump index 

#List Comprehension
# number=[i for i in range(10) if i%2==0]
# print(number)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)
