
a=input("ENter the string : ")
inp=int(input("Enter the 1 for coding and 0 for decoding :"))


if(inp==1):
   
   if(len(a)>=3):
    print("abd"+a[1:]+a[0]+"xyz")
   else:
    print(a[::-1])
elif(inp == 0):
    if(len(a)>=3):
       print(a[-4]+a[3:len(a)-4])
    else:
      print(a)





