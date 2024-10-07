# write a library class with no_of_books and booksa as two instance variable. write a program to create a library from this library class and show how you can print all books,
# and book and get the number of books using different methods. show that your program doesnt persist the book after the program it stopped.

class library:
    def __init__(self):
        self.nobooks = 0
        self.books = []
        
    def addbooks(self, book):
        self.books.append(book)
        self.nobooks = len(self.books)
        
    def showInfo(self):
       print(f"the library has {self.nobooks} books and the books are")
       for book in self.books:
           print(book)
       
l1 = library()
l1.addbooks("the yogi")
l1.addbooks("the lion")
l1.addbooks("the tiger")
l1.showInfo()