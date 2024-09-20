
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
    def list_of_books():
        return sql.find_all_books()

    @classmethod
    def book_number(cls):
        return Book.number_of_books 




    def __del__():
         pass
    

