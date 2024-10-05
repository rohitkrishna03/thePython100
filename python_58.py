# inheritance in python

# when a class derives from another class. the child class will inherit the public adn protected properties and methods from the parent class.
# in addition, it can have its own properties and methods, this is called as inheritance.
# types of inheritance:-
# single inheritance
# multiple inheritance
# multilevel inheritance
# hierarchical inheritance


class employee:
    def __init__(self, name , id):
        self.name = name
        self.id = id
        
    def showDetails(self):
            print(f"the name if the employee is {self.name} and id is {self.id}")
            
class programmer(employee):
    def showlanguage(self):
        print("the default language is python")
        
    
e1 = employee("rohit", 400)
e1.showDetails()
e2= programmer("krishns", 500)
e2.showDetails()
e2.showlanguage()
