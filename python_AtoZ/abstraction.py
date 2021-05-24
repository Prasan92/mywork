
class Liberary:
    def __init__(self,listofbooks):
        self.listofbooks = listofbooks

    def display_books(self):
        print("available books: ")
        for books in self.listofbooks:
            print (books)

    def lend_books(self, requestedbook):
        print("available books: ")
        if requestedbook in self.listofbooks:
            print ("you have borrowed the book")
            self.listofbooks.remove(requestedbook)
        else:
            print("sorry, book not available")

    def add_books(self, returnedbook):
        self.listofbooks.append(returnedbook)
        return self.listofbooks


class Customer:
    def request_books(self):
        print("enter the name book: ")
        self.book = input ()
        return self.book

    def return_books(self):
        print("enter name of the book: ")
        self.book = input ()
        return self.book


lib = Liberary(["harry potter","lord of the rings","alice in the wonderland"])
cus = Customer()

while True:
    print("enter 1 to display the available books")
    print("enter 2 to request a book")
    print("enter 3 to return a book")
    print("enter 4 to exit")
    userchoice = int(input())
    if userchoice == 1:
        lib.display_books()
    elif userchoice == 2:
        requestedbook = cus.request_books()
        lib.lend_books(requestedbook)
    elif userchoice == 3:
        returnedbook = cus.return_books()
        lib.add_books(returnedbook)
    elif userchoice == 4:
        quit()


