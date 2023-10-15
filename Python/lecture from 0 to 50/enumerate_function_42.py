marks=[12,34,53,59,20,78,50]
# index=0
# for marks in mark:
#     print(marks)
#     if(index==3):
#         print("Momin taufeeq")
#     index+=1
#Enumerate mean if we want to print through index
for index,mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("Momin Taufeeq")
#For exmaple:--
lis=["Apple","Mango","Banana","Orange"]
for index,lit in enumerate(lis,start=1):#start is use start the index from 1
    print(index,lit)

