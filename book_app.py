
import books_sqlite as sql

class Book:
    """
    This class is for managing books
    such as add , delete and find them from database.
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
        if len(str(val))==8 and type(val) == int:
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

    

