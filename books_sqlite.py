import sqlite3
from sys import path

database = sqlite3.connect(path[0]+"/books_db.db")
cursor = database.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS books_table(ISBN INTEGER PRIMARY KEY\
                   ,title TEXT,author TEXT,price FLOAT,pages INTEGER)")
    
def insert_book(ISBN , title , author , price , pages):
    try:
        cursor.execute("INSERT INTO books_table VALUES(?,?,?,?,?)"\
                    ,(ISBN , title , author , price , pages)) 
        database.commit() 
    except(sqlite3.IntegrityError): 
        print("ISBN is a UNIQE number !")    



def serach_book(ISBN):
    abook=()
    abook= cursor.execute("SELECT * FROM books_table WHERE ISBN==?",[ISBN]).fetchone()
    if abook is None:
       return ("This book with this isbn does not exists!")
    else:
        return abook  


def find_all_books():
    return list(cursor.execute("SELECT * FROM books_table"))


    
def delete(ISBN):
    abook=()
    abook= cursor.execute("SELECT * FROM books_table WHERE ISBN==?",[ISBN]).fetchone()
    if abook is None:
        return("This book with this isbn does not exists!")
    else:
        cursor.execute("DELETE FROM books_table WHERE ISBN==?",[ISBN])
        database.commit()
        return "Book successfully deleted !"
        

