n=int(input("ENter the number :"))
if(n%2==0):
    if(n>2 &n<5):
     print("Not Weird,range of 2,5")
    if(n>6 &n <20):
        print(" Weird,range of 6 to20")
    if(n>20):
        print("Not Weird, greater than 20")
else:
    print("Weird")