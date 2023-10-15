#Without using Function
# a=9
# b=8
# gmean=(a*b)/(a+b)
# print(gmean)

#Using Function
def CalculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def isGreater(a,b):
    if(a>b):
        print("First Number is Greater")
    else:
        print("Second Number is Greater")
def islesser(a,b):
    pass # using pass we can create function after word .If we does not use pass it show an error
    

a=9
b=15
isGreater(a,b)
CalculateGmean(a,b)
c=15
d=12
isGreater(c,d)
CalculateGmean(c,d)
def Ifstatement(y,z):
    if(y<z):
        print("first value is less than second")
    elif(y>z):
        print("firstvalue is Greater than second")
    else:
        print("first is equal to second")
# y=int(input("Enter the number of Y : "))
# z=int(input("Enter the number of z : "))
# Ifstatement(y,z)
a=10
b=20
Ifstatement(a,b)
