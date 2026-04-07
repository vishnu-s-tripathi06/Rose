class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def list_books(self):
        result = []
        for every_book in self.books:
            result.append(f"{every_book.title} by {every_book.author}")
        return result
class Book:
    def __init__(self,title,author):
        self.author=author
        self.title=title


book1=Book("Harry Potter","JK rowlings")
book2=Book("Lord of the rings","J.R.R Tolkein")
Govind=Library("Govind Public Library")

Govind.add_book(book1)
Govind.add_book(book2)
for i in Govind.list_books():
    print(i)