# In Python, a lambda function is a small anonymous function without a name. 
'''Lambda functions are often used in situations where a small function is 
required for a short period of time. 
They are commonly used as arguments to higher-order functions, such as map, filter, and reduce'''
#lambda 
# is a function .When we lambda we will create function in one line 
# def double(x):#Whitout using lambda function
#     return x*2
# print(double(5))

#Using Lambda Function :-
# double=lambda x : x*2
# print(double(5))
# square=lambda x: x*x
# print(square(5))
# cube=lambda x:x*x*x
# print(cube(5))

#We can use multiple varible at a time.Lambda function is written in one 
# avg=lambda x,y,z:(x+y+z)/3
# print(avg(5,3,10))

# def appl(fx,value):
#     return 6+ fx(value)
# print(appl(lambda x:x*x*x,2))#There is no need to create a function of cube it will work directly .

# Lambda functions can also include multiple statements, but they are limited to a single expression.
#  For example:
# Lambda function to calculate the product of two numbers,
# with additional print statement
# lambda x, y: print(f'{x} * {y} = {x * y}')




