# First of all, create a UML diagram of the domain.
# You're free to choose classes and names to model,
# but be sure to include classes Book and Shelf.
# Bob's room is a collection of shelves.

# Code up your classes from the diagram.
# Then, start organizing (write a separate function for each step):

class Book(object):

    def __init__(self, title, category, author):
        self.title = title
        self.author = author
        self.category = category


class Shelf(Book):

    def __init__(self):
        self.categories = []
        self.books = []

    def add_book(self, book):
        if book.category in self.categories:  # Add the book if the shelf has its category           self.books.append(book)

    def show_books(self):
        for category in self.categories:
            print(f"Category: {category}")
            for book in self.books:
                if book.category == category:
                    print(f"  - {book.title}, {book.author}")

# Create a couple of books (e.g. with Faker library or manually)
# to show that your program works.

books_DB= [
    Book("Book1", 'Art', "Author1"),
    Book("Book8", 'Science', "Author2"),
    Book("Book7", 'Fiction', "Author3"),
    Book("Book5", 'Poetry', "Author4"),
    Book("Book6", 'Art', "Author5"),
    Book("Book4", 'Art', "Author6"),
    Book("Book3", 'Science', "Author1"),
    Book("Book2", 'Poetry', "Author8")
]

shelfs_DB = [
    Shelf(),
    Shelf(),
    Shelf()
]

# TASK 1. Starting with a huge pile (set) of books,
# organize them into the shelves by category.

# There can be more categories than books,
# so one shelf can contain multiple categories.
# But books of the same category must always be on the same shelf.


def organize_books(books: list, shelfs: list):

    categories_list = [] # defining all existing categories in set

    for book in books:
        if book.category not in categories_list:
            categories_list.append(book.category)

    for i in range(len(categories_list)): # distributing categories between shelfs
        j = i % len(shelfs) # calculating index of shelf
        shelfs[j].categories.append(categories_list[i])

    for book in books:
        for shelf in shelfs:
            shelf.add_book(book)

    for shelf in shelfs:
        print(f'Shelf with index #{shelfs.index(shelf)}')
        shelf.show_books()


print('***Task 1***')
organize_books(books_DB, shelfs_DB)

# 2. Iterate over all the shelves and sort the books
# by title in ascending order.

print('***Task 2***')
for shelf in shelfs_DB:
    shelf.books.sort(key=lambda x: x.title, reverse=False)
    print(f'Shelf with index #{shelfs_DB.index(shelf)}')
    shelf.show_books()
