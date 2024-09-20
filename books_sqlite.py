import sqlite3
from sys import path

database = sqlite3.connect(path[0]+"/books_db.db")
cursor = database.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXIST books_table(ISBN INTEGER PRIMARY KEY\
                   ,title TEXT,author TEXT,price FLOAT,pages INTEGER)")
    
def insert_book(ISBN , title , author , price , pages):
    cursor.execute("INSERT INTO books_table VALUES(?,?,?,?,?)"\
                   ,(ISBN , title , author , price , pages)) 
    database.commit()  

def find_book(ISBN):
    return cursor.execute("SELECT * FROM books_table WHERE ISBN==?",[ISBN]).fetchone() 

def find_all_books():
    return list(cursor.execute("SELECT * FROM books_table"))



def delete_book(ISBN):
    cursor.execute("DELETE FROM books_table WHERE ISBN==?",[ISBN])
    database.commit()

