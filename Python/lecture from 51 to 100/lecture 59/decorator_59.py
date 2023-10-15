'''Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods.
 They are a way to extend the functionality of a function or method without modifying its source code.'''





# def greet(fx):
#     def mfx(*args ,**kwargs):
#      #*args :- Jitne bhi arrgument hai unko lene ka tarika hai as a tuple.
#      #**kwargs :-as a dictionary sare argument ko lene ka tarika hai key value pair ke tor par
#      print("Good Morning")
#      fx(*args,**kwargs)
#      print("Thank You")
#     return mfx
    
# @greet
# def hello():
#  print("Hello World")

# @greet
# def add(a,b):
#   print(a+b)

# hello()
# # greet(add)(1,2)#We can write this way also
# add(1,2)


import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b














