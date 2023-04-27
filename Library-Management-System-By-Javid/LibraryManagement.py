import sqlite3
from LibraryDatabse import Database
conn = Database.conn
class Library:
    books = []
    my_book = {}
    def getAllBooks(self):
        crsr = conn.cursor()
        sql = f"SELECT BookName FROM books"
        crsr.execute(sql)
        self.books = crsr.fetchall()
    def addBook(self,book,author):
        crsr = conn.cursor()
        sql = f"INSERT INTO books(BookName,AuthorName) VALUES(?,?)"
        values = (book,author)
        crsr.execute(sql,values)
        pass
    def getBookByAuthourName(self,author):
        crsr = conn.cursor()
        sql = f"SELECT BookName FROM books WHERE AuthorName = '{author}'"
        crsr.execute(sql)
        books = crsr.fetchall()
        print("The available books are\n-----------------------")
        for book in books:
            print("\t",*book)
        pass 
    def sortBooksByTopologicalOrder():
        pass
    def getAllSubscribers():
        pass
    def getAllEarnigns():
        pass
    def getUnAvailabelBooks():
        pass
    def mapAuthorWithBook():
        pass
Library().getAllBooks()
Library().getBookByAuthourName("Bjarne Straoustrap")

class MyLibrary(Library):
    def getFavouriteBook():
        pass
    def getFavoriteCustomer():
        pass
    