# Simple Factory Pattern in the style of a notifier system

# Define the Notifier Interface
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, to: str, message: str) -> str:
        pass

# Concrete Notifiers
class EmailNotifier(Notifier):
    def send(self, to: str, message: str) -> str:
        return f"Email sent to {to}: {message}"

class SMSNotifier(Notifier):
    def send(self, to: str, message: str) -> str:
        return f"SMS sent to {to}: {message}"

# Notifier Factory
class NotifierFactory:
    @staticmethod
    def create(kind: str) -> Notifier:
        if kind == "email":
            return EmailNotifier()
        elif kind == "sms":
            return SMSNotifier()
        else:
            raise ValueError("Unsupported notifier type")

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
    def __init__(self, notifier: Notifier):
        self._catalog = {}
        self._loans = {}
        self._notifier = notifier

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
            message = f"{member.name} borrowed '{book.title}'"
            print(self._notifier.send(member.email, message))
        else:
            print(f"Book {isbn} is not available.")

    def return_book(self, member, isbn):
        if isbn in self._loans.get(member.email, set()):
            self._catalog[isbn].available = True
            self._loans[member.email].remove(isbn)
            message = f"{member.name} returned '{self._catalog[isbn].title}'"
            print(self._notifier.send(member.email, message))
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




# Notifier System
# Create notifier via factory
notifier = NotifierFactory.create("email")

# Create library with notifier
library = Library(notifier)

# Create people
librarian = PersonFactory.create_person("librarian", "Ada", "ada@library.com")
member = PersonFactory.create_person("member", "Tunde", "tunde@email.com")

# Add books and register member
librarian.add_book(library, Book("Things Fall Apart", "Chinua Achebe", "ISBN001"))
librarian.register_member(library, member)

# Borrow and return with notifications
member.borrow_book(library, "ISBN001")
member.return_book(library, "ISBN001")



