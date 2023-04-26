



class Book:
    numberOfPages = 145
    author = "sudhanshu"
    scope = "To be sold in india"

    def __init__(self , zone , dob):
        self.zone = zone
        self.dob = dob
    def __del__(self):
        print("destructor is called")

my_book = Book("Mystery","25-10-1998")
print(my_book.numberOfPages)
print(my_book.zone)
print(my_book.dob)
del my_book
