# Write a program to accept a string from the user and display characters that are present
#  at an even index number.

user=input("Enter the String :")
print(len(user))
for i in range(0,len(user)):
    if(i%2==0):
        print(user[i])


   