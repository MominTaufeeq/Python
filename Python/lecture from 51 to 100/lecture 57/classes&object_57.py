# A class is a blueprint or a template for creating objects, providing initial values for state 
# (member variables or attributes), and implementations of behavior (member functions or methods).
#  The user-defined objects are created using the class keyword.
class Person:#Creating Class
    name="Taufeeq"
    age="19"
    occupation="Bca "
    def info(self):#self is a parameter .self mean wo object jis ke liye method call kiya jaraha hai
        print(f"{self.name} is a {self.age}")

a=Person()#Creating Object.We can create multiple object like this 
b=Person()
c=Person()
b.name="Uzair"
b.age="9"
a.name="Momin"#Changing the name
a.age="20"
print(a.name)
print(a.age)
a.info()#Calling a function
b.info()
c.info()#If we have not given value for c then it will default value