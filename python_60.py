# static method :
# static method in python are method that belongs to a class rather than an instance of class.
# they are defined using the @staticmethod decorator and donot have access to the instance of the class9i.en self
# theya are called on the class itself, not on a instance of the class.
# static method are often used to create utility function that dont need access to inheritance data.

# class math:
#     @staticmethod
#     def add(a,b):
#         return a+b
    
# result = math.add(1,2)
# print(result)

# in the abive example, the add method is static method of the math class. t takes two parameters a and b their sum.
# the method can be called on the class itself, without the need to create an instance of the class.
#

class Math:
    def __init__(self,num) :
        self.num=num
        
    def addtonum(self, n):
        self.num =self.num+n
    @staticmethod
    def add(a,b):
        return a+b
    
    
    # result = math.add(1,2)
    # print(result)
    
a= Math(5)
print(a.num)
a.addtonum(6)
print(a.num)