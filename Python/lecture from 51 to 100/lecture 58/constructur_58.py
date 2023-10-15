# A constructor is a special method in a class used to create and initialize an object of a class.
# There are different types of constructors. Constructor is invoked automatically when an object of a class is created.

# A constructor is a unique function that gets called automatically when an object is created of a class.
# The main purpose of a constructor is to initialize or assign values to the data members of that class.
#  It cannot return any value other than None.
class Person():
    def __init__(self ,n,o):#Use to create a construtor using a special keyword is "__init__()".In a bracket there is argument
        print("Hey this is pass")
        self.name=n
        self.occu=o
    def info(self):
        print(f"{self.name} is a {self.occu}")
#Self argument  is automatically pass ho raha hai .That why we need to pass only two argument
a=Person("Taufeeq","developer")
b=Person("Momin","deve")
a.info()
b.info()

#There are two type of constructor 
# 1)Parameterized Constructor:-upone eg is a parmeterized constructor .def __init__(self,name,occu): this is parame
# 2)Default Constructor:-lecture 57 is the eg. of default constructor .def __init__(self): this is default