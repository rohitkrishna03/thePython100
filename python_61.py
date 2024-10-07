# instance  vs static method in python
# in python variables can be defined at the class or at the instance level.
# understanding the difference between these types of variables is crucial for writing efficient and maintainance code.

# class variable:
# class variable are defined at the class level and are shared among all instance of the class.
# they are defined outside of any method and are usually used to satire information that is common to all instance of the class.
# for example, a class variable can be used to store the number of instances of a class that have been created.
# 

class employee:
    companyname = "apple"
    noOfEmployee =0
    def __init__ (self, name):
        self.name=name
        self.raise_amount=0.02
        employee.noOfEmployee +=1
    def showDetails(self):
            print(f"the name of the employee is {self.name} and the raise amount in {self.noOfEmployee} sized {self.companyname} is {self.raise_amount}")

emp1 = employee("rohit")
emp1.raise_amount =0.3
emp1.showDetails()
emp1.companyname ="apple india"
emp2 = employee("rohit")
emp2.showDetails()
employee.companyname ="meta"
print(employee.companyname)

# if they are defined on the instance level then they are called as instance variable.