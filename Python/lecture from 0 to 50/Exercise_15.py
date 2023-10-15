import time

t=time.strftime("%H:%M:%S")
hours=int(time.strftime("%H"))
print(hours)
hours=int(input("Enter the hours"))
if(hours>=0 and hours < 12): 
    print("Good Morning sir")
elif(hours>=12 and hours <17): 
    print("Good evening sir")
elif(hours >=17 and hours < 24):
    print("Good Night Sir")

# hours=input("Enter the hours : ")
# min=input("Enter the minutes :")
# second=input("Enter the second :")
# dayornight=input("Enter Am/Pm :")
# Goodmorning="11:59 am"
# GoodEvening="6:00 pm"
# time=hours +":" +min+":"+second+" "+ dayornight
# if( time <= Goodmorning):
#     print("Good Morning")
# elif(hours and min and second and dayornight <GoodEvening):
#     print("Good Evening")
# else:
#     print("Good Night")
# print(time)

# Goodmorning="11:59 am"
# GoodEvening="6:00 pm"
# if(time <= Goodmorning ):
#     print("Good Morning")
# elif(time<=GoodEvening):
#     print("Good Evening")
# else:
#     print("Good night")
