class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def DetailEmp(self):
        print(f"Employee name is: {self.name} and id is {self.id}")

e1=Employee("Taufeeq",40)
e1.DetailEmp()
e2=Employee("Taufee",60)
e2.DetailEmp()

#We can create new class with oid class employee
# for eg:
class Programmer(Employee):
    def newDetail(self):
        print(f"New class Name using{self.name} and id :{self.id}")
e3=Programmer("Momin",15)
e3.DetailEmp()#We can also called old class
e3.newDetail()
class newProgrammer(Programmer):
    def newPDetail(self):
        print(f"This is newProgram {self.name} and id {self.id} ")
e4=newProgrammer("uzair",0)
e4.newPDetail
        