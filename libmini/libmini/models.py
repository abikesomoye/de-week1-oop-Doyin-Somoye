# 1. Base class
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"{self.__class__.__name__}(Name: {self.name}, Email: {self.email})"

# 2. Subclasses
class Member(Person):
    def borrow_book(self, library, isbn):
        library.borrow(self, isbn)

    def return_book(self, library, isbn):
        library.return_book(self, isbn)

class Librarian(Person):
    def register_member(self, library, member):
        library.register_member(member)

    def add_book(self, library, book):
        library.add_book(book)

# 3. Book class
class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __repr__(self):
        status = "Available" if self.available else "Checked Out"
        return f"Book({self.title}, {self.author}, ISBN: {self.isbn}, {status})"

# 4. Library class
class Library:
    def __init__(self):
        self._catalog = {}  # isbn -> Book
        self._loans = {}    # email -> set of isbn

    def add_book(self, book):
        self._catalog[book.isbn] = book

    def register_member(self, member):
        if member.email not in self._loans:
            self._loans[member.email] = set()

    def borrow(self, member, isbn):
        book = self._catalog.get(isbn)
        if book and book.available:
            book.available = False
            self._loans[member.email].add(isbn)
        else:
            print(f"Book {isbn} is not available.")

    def return_book(self, member, isbn):
        if isbn in self._loans.get(member.email, set()):
            self._catalog[isbn].available = True
            self._loans[member.email].remove(isbn)
        else:
            print(f"{member.name} did not borrow book {isbn}.")

    def member_loans(self, member):
        return [self._catalog[isbn] for isbn in self._loans.get(member.email, set())]

# 5. Simple Factory
class PersonFactory:
    @staticmethod
    def create_person(role, name, email):
        if role == "member":
            return Member(name, email)
        elif role == "librarian":
            return Librarian(name, email)
        else:
            raise ValueError("Unknown role")



# Step 1: Setup the Library and Factory
library = Library()

# Create a librarian and a member using the factory
librarian = PersonFactory.create_person("librarian", "Ada", "ada@library.com")
member = PersonFactory.create_person("member", "Tunde", "tunde@email.com")

# Step 2: Librarian Adds Books
book1 = Book("Things Fall Apart", "Chinua Achebe", "ISBN001")
book2 = Book("Half of a Yellow Sun", "Chimamanda Ngozi Adichie", "ISBN002")

librarian.add_book(library, book1)
librarian.add_book(library, book2)

# Step 3: Librarian registers Member
librarian.register_member(library, member)

# Step 4: Member Borrows a Book
member.borrow_book(library, "ISBN001")
print("Tunde's Loans:", library.member_loans(member))


# Step 5: Member Returns the Book
member.return_book(library, "ISBN001")
print("Tunde's Loans After Return:", library.member_loans(member))



