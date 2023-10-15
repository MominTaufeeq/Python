#Seek Function
# with open("file51.txt",'r') as f:
#     print(type(f))
#     f.seek(10)

#     data=f.read(5)
#     print(data)

#tell Function
# with open("file51.txt",'r') as f:
#     print(type(f))
#     f.seek(10)
#     print(f.tell())
#     data=f.read(5)
#     print(data)

#Truncate function
with open("truncate51.txt",'w') as f:
   f.write("Hello World")
   f.truncate(5)#It will only print 5 character from stating 

with open('truncate51.txt','r') as f:
   print(f.read())
   
