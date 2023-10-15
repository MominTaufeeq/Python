'''Getters in Python are methods that are used to access the values of an object's properties.
 They are used to return the value of a specific property, and are typically defined using the @property decorator.
 Here is an example of a simple class with a getter method:'''
class MyClass:
    def __init__(self, value):
        self._value = value
    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return 10 *self._value
    '''It is important to note that the getters do not take any parameters and we cannot set the value through getter method.
     For that we need setter method which can be added by decorating method with @property_name.setter'''
    @ten_value.setter
    def ten_value(self,new_value):
        self._value=new_value/10
    @ten_value.setter
    def ten_value(self,new_value):
        self._value=new_value/20
obj=MyClass(10)
# print(obj.ten_value)
obj.ten_value=67

obj.show()
