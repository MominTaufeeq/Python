#Map
# def cube(x):
#     return x*x*x

# print(cube(2))

# l=[2,4,8,30,3,5]
# new=[]
# for iteam in l:
#     new.append(cube(iteam))
# print(new)

#Using Map 
# new=list(map(cube,l))
# new=list(map(lambda x: x*x*x ,l))#Using Lamda function
# print(new)

# #Filter
# def filter_function(a):
#     return a>3
# newf=list(filter(filter_function,l))
# print(newf)

#Reduce 
from functools import reduce
number=[1,2,3,4,5]
sum=reduce(lambda x,y :x+y ,number)
print(sum)
