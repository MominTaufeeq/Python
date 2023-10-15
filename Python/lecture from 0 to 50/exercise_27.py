
# option=['How many states are there in India'
#         ,'A.35','B.28','C.25','D.30']
# option1=["How many country are there in the world ","A.300","B.200","C.250","D.195"]

# print(option[0])
# print(option[1])
# print(option[2])
# print(option[3])
# print(option[4])

# user=input("Enter You option :")
# if("A" in user):
#     print("This is wrong answer")
# elif("B" in user):
#     print("This is Right answer \nYou Have Won 20,000")
# elif("C" in user):
#     print("This is wrong answer")
# elif("D" in user):
#     print("This is Wrong answer")

    
# print("Next  Question is ",option1[0])

# print(option1[1])
# print(option1[2])
# print(option1[3])
# print(option1[4])



# user1=input("Enter You option :")
# if("A" in user1):
#     print("This is wrong answer")
# elif("B" in user1):
#     print("This is Wrong answer")
# elif("C" in user1):
#     print("This is wrong answer")
# elif("D" in user1):
#     print("This is Right answer\n You won 40,000")
question=[
    ["How many states are there in India","35","28","25","30",2],
    
    ["How many states are there in India","35","28","25","30",2],
    ["How many states are there in India","35","28","25","30",2],
    ["How many states are there in India","35","28","25","30",2],
    ["How many states are there in India","35","28","25","30",2]

]
# levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
# money = 0
# for i in range(0, len(questions)):
  
#   question = questions[i]
#   print(f"\n\nQuestion for Rs. {levels[i]}")
#   print(f"a. {question[1]}          b. {question[2]} ")
#   print(f"c. {question[3]}          d. {question[4]} ")
#   reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
#   if (reply == 0):
#     money = levels[i-1]
#     break
#   if(reply == question[-1]):
#     print(f"Correct answer, you have won Rs. {levels[i]}")
#     if(i == 4):
#       money = 10000
#     elif(i == 9):
#       money = 320000
#     elif(i == 14):
#       money = 10000000
#   else:
#     print("Wrong answer!")
#     break 

# print(f"Your take home money is {money}")
level=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000]
money=0
for i in range(0,len(question)):
    question=question[i]
    print(f"\n\nQuestion for Rs. {level[i]}")
    print(question[0])
    print(f"a. {question[1]}        b.{question[2]}")
    print(f"c. {question[3]}        c.{question[4]}")
    reply=int(input("Enter your answer( 1-4) or 0 to quit:\n"))
    if(reply == 0):
        money=level[i-1]
        break
    if(i==4):
        money=10000
    elif(i==9):
        money=320000
    else:
        print("Wrong anwser")
        break
   

