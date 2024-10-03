# OOPS(OBJECTED ORIENTED PROGRAMMING LANGUAGE)

# THERE ARE MAINLY TWO APPROACHES OF WRITING A CODE WHICH ARE:
# PROCEDURAL PROGRAMMING
# OBJECT ORIENTED PROGRAMMING 

# a procedural we are following til now ois the "procedural programming " approach. so, in this secessin, we will lean about oops
# the basic idea of oops sto use the concept of class and objects to represent the real-world concept and entities.

# a class is the blue print or template for creating objects, it defines the propertirs and methods that an object of the class will have.
# properties ae the data or state od an object, and method are the actions or behavior that an object can perform.

# an object is an instance of class, and it cointains its own data and method, ofr exapmle, you could create a class called "person" that has properties such as name and age, method such as speak()
# walk().
# each instance of a person class would have unique object with its own  name and age
# but they would all have the same method like speak and walk.


# class and objects

class person():
    name ="rohit"
    age =25
    job = "web developer"
    
    # self is a parameter is the reference to the current instance of the class.
    
    def info(self):
        print(f"{self.name} is a {self.job}")
        # id i want to change the name and job we can do like this
       
a=person()
a.name ="lion"
a.job ="king"
        
a.info()