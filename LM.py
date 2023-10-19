class Library:
    def __init__(self,list,name):
        self.booksList=list
        self.name=name
        self.lendDict={}
    def dispalyBooks(self):
        print("we have following books in our library:{self.name}")
        for book in self.booksList:
            print(book)
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated.u can take the book now")
        else:
            print("book is already being used by {self.lendDict[book]}")
    def addBook(self,book):
        self.booksList.append(book)
        print("Book has been added to the book list")
    def returnBook(self,book):
        self.lendDict.pop(book)
if __name__=='__main__':
    sak=Library(['Python','Maths','C','C++','Java'],'SAK')

    while(True):
        print("welcome to the {sak.name} library.Enter your choice to continue")
        print("1.Display Books")
        print("2.Lend a  book")
        print("3.Add a  book")
        print("4.Return a  book")
        user_choice=input()
        if user_choice not in ['1','2','3','4']:
            print("please enter a valid option")
            continue
        else:
            user_choice=int(user_choice)
            if user_choice == 1:
                sak.displayBooks()
            elif user_choice == 2:
                book=input("Enter the name of the book you want to lend:")
                user=input("Enter your name")
                sak.lendBook(user,book)
            elif user_choice == 3:
                book=input("Enter the name of the book you want to  add")
                sak.addBook(book)
            elif user_choice == 4:
                book=input("Enter the name of the book you want to return")
                sak.returnBook(book)
            else:
                print("not valid option")
        print("press q to quit and c to continue")
        user_choice==""
        while(user_choice!="c" and user_choice!="q"):
            user_choice=input()
            if user_choice == "q":
                exit()
            elif user_choice == "c":
                continue
