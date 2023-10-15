# a=int(input("Enter your age : "))
# print("Your Age is ",a)
# #Conditional Operator
# #>,<,>=,<=,!=
# if(a>18):
#     print("You can Drive A car")
# else:
#     print("You Cannot Drive a car")
#if-else-elif
# num=int(input("Enter the value"))
# if(num<0):
#     print("Num is Negative")
# elif(num==0):
#     print("Num is equal to zero")
# else:
#     print("Num is positive")
#Nested If
num=int(input("ENter the number"))

if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
