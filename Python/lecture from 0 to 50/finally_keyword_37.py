# def fun():
#     try:
#         l=[5,1,6,8]
#         a=int(input("Enter the number :"))
#         print(l[a])
#         return 1
#     except:
#         print("error occur")
#         return 0
#     finally:# finally ka matlab agar function koi error aajai to to bhi print hoga or nahi aaye to bhi print hoga
#         print("If we have written in function or out of function it print ")
# #Agar sirf mai print statement use karta jab error aata to print nahi hoti line Or agar error nahi aata to
# #print hoja ti line
    
# x=fun()
# print(x)
#eg:-
def fun1():
 try:
    l=[9,4,6,0]
    a=int(input("ENter the number"))
    print(l[a])
    return 1
 except:
    print("Error")
 return 0
 print("We doesnot use finally keyword in function it  occur error it does not print ")
x=fun1()
print(x)


   