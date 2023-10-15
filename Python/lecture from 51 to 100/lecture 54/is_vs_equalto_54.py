'''is and == , is a comaprision operator.
'is' is a exact location of memory .
'==' value .'''
'''If we are taking a=3,b=3 than it will return true but if we are taking in list then 'is'
will return false when we have taken list ,If Both variable value is same than it store in memory 
at same location eg:- a=3,b=3 it will store at same location'''
#List
#  a=[1,2,3]
# b=[1,2,3]
# print(a is b)#It will return  false .because the value can change/mutable in list
# print(a==b)
#tuple 
a=(3,4,5)
b=(3,4,5)
print(a is b)#It will return true. Because the value immutable/not changeable
print(a == b)


