
import books_sqlite as sql

class Book:
    """
    HELLO
    """
    number_of_books = 0

    def __init__(self, ISBN , title , author , price , pages ):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages   
        Book.number_of_books+=1 
        sql.insert_book(self.ISBN , self.title ,self.author , self.price ,self.pages)

    @property
    def ISBN(self):
        return self._isbn
    @ISBN.setter
    def ISBN(self , val):
        if len(str(val))==8:
            self._isbn = val
        else:
            raise ValueError("ISBN must have 8 digits !")    
    
 
    @staticmethod
    def find_book(isbn):
        return sql.serach_book(isbn)


    @staticmethod
    def list_of_books():
        return sql.find_all_books()

    @staticmethod
    def delete_book(isbn):
        return sql.delete(isbn)

    @classmethod
    def book_number_you_add(cls):
        return str(cls.number_of_books )

    def __del__():
         pass
    
# try:
#       book1 = Book(12345678 , "f", "d", 5, 100)
#     # book2 = Book(12345679 , "ff", "dd", 55, 1000)
#     # book3 = Book(12345670 , "fff", "ddd", 555, 10000)
# except(ValueError):
#     print("ISBN must have 8 digits !")

