from aggregation import Library,Book
library = Library("New York Public Library")

Book1 = Book("Harry Potter", "J.K. Rowling")
Book2 = Book("The Hobbit", "J.R.R. Tolkien")
Book3 = Book("The Color of Magic", "Terry Pratchett")

library.add_book(Book1)
library.add_book(Book2)
library.add_book(Book3)

print(library.name)

for book in library.list_books():
    print(book)