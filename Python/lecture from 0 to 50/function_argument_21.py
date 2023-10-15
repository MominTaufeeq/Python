'''There  are four type of argumnent
1) defual Argumnet
2) Keyword Argument
3) Variable lenght Argumnet
4) Required argument'''
# 1) Default Argument
# def Average(a=10,b=2):#default value 
#     print("The Average is " ,(a+b)/2)

# #Average(6)#It take value of a
# Average(b=4)#It will change the value of b
# def Name(fname,mname="Taufeeq",lname="Tayyab"):
#     print("Hello ",fname,mname,lname)

# Name("Momin")#It take the value of fname 
# Name("Momin","Uzair")#It will change the value of mname
# def name(fname,mname,lname):
#     print("HEllo ",fname,mname,lname)

# name("Momin","Taufeeq")


def average(*number):#single star is called as a tuple
    print(type(number))
    sum=0
    for i in number:
        sum= sum +i
    # print("Average is :",sum/len(number))
    return sum/len(number)
c=average(5,6,7)
print(c)



# def name(**name):
#     print("Your Name is",name["fname"],name["mname"],name["lname"])

# name(mname="Tayyab ali",fname="Taufeeq",lname="Momin")



