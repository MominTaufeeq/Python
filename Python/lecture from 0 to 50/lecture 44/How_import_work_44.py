# import math
# result=math.sqrt(9)
# print(result)

#From is use keyword is to import specific function or variable from module using from keyword
# from math import sqrt
# result=sqrt(9)
# print(result)

#If we want to take two function or variable it is seprated by comma
# from math import sqrt,pi
# result=sqrt(9)*pi
# print(result)

'''It's also possible to import all functions and variables from a module using the * wildcard.
However, this is generally not recommended as it can lead to confusion and make it harder to 
understand where specific functions and variables are coming from.'''
# from math import *

"as keyword "
# from math import pi,sqrt as s
# result=s(9)*pi
# print(result)

# import math as m
# result=m.sqrt(9)
# print(result)

'''dir :- It is a function.Is use to print all function and method thing of which we have imported for eg'''
# import math
# print(dir(math))
# print(math.nan,type(math.nan))
'''import fuction which made by us'''
# from us_function_44 import welcome,taufeeq
from us_function_44 import *
welcome()
print(taufeeq)


