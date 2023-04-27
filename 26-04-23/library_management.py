class Library:
    book = ["The fault in our stars" , "Abang" , "Citadel"]
    author_book = {
        "Pablo":["escobar","escobar returns","escobar part 3"]
    }
    def getAllBooks():
        pass
    def addBook():
        pass
    def getBookByAuthorName(authorName):
        for key in author_book:
            if key == authorName:
                print(author_book[key])


    def sortBooksInTopologicalOrder(self):
        book_copy = []
        for books in self.book:
            book_copy.append(books)

        return book_copy.sort()

    def getAllSubscribers():
        pass
    def getAllEarnings():
        pass
    def getUnavailableBooks():
        pass
    def mapAuthorWithABook():
        pass
class MyLibrary(Library):
    # it can not have it's own data structure to store book , authors , subscribers , unvailable books
    def getFaviourtBook():
        pass
    def getFaviourtCustomer():
        pass
