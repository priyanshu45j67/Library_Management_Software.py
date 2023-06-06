'''library management software'''
class library:
    def __init__(self):
        self.no_of_book=0
        self.books=[]
    def addbook(self,book):
        self.books.append(book)
        self.no_of_book=len(self.books)
    def show(self):
        print(f"The library has {self.no_of_book} books")
        for i in self.books:
            print(i)
obj=library()

num=int(input("Enter the no of book add "))
for i in range(num):
    book_name=input("Enter the book name ")
    obj.addbook(book_name)

obj.show()
