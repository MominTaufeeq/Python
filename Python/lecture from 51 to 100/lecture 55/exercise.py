# computer=   s w g
#user:-    s  2 0 1
#          w  1 2 0
#          g  0 1 2
match=[0,1,2]
snake="s"
water="w"
gun="g"

user=input("Enter the one number : ")

for i in match:
    if(user == snake):
        if(user[0] == match[2]):
            print("Match Draw ")
        elif(user[0] == match[0]):
            print("Win The Match ")
        elif(user[0] == match[1]):
            print("Loss the Match")
    elif(user == water):
        if(user[0] == match[1]):
            print("Match Draw ")
        elif(user[0] == match[2]):
            print("Win The Match ")
        elif(user[0] == match[0]):
            print("Loss the Match")
    elif(user == gun):
        if(user[0] == match[2]):
            print("Match Draw ")
        elif(user[0] == match[0]):
            print("Win The Match ")
        elif(user[0] == match[1]):
            print("Loss the Match")
    print(i)
     
    

    
