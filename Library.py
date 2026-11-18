class Library:

    total_books = 0
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        Library.total_books += 1

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            return f"Successfully borrowed '{self.title}'. Remaining copies: {self.copies}"
        return f"Sorry, '{self.title}' is currently out of stock."
    def return_books(self):
        self.copies += 1
        return f"Successsfully returned '{self.title}'. Availabe copies: {self.copies}"
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.copies} available)"
    def __repr__(self):
        return f"Library('{self.title}', '{self.author}', {self.copies})"

if __name__ == "__main__":
    print("=== LIBRARY TEST===")

    book1 = Library ("Noli Me Tangere", "Jose Rizal", 3)
    book2 = Library ("El Filibusterismo", "Jose RIzal", 4)

    print(book1)
    print(book1.borrow())
    print(book1.borrow())
    print(book1.return_books)
    print()
    print(book2)
    print(book2.borrow())
    print()
    print(repr(book1))
    print(f"Total book created: {Library.total_books}")