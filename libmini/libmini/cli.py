from libmini.models import Book, Library, PersonFactory
from libmini.notify import NotifierFactory

def main():
    # Create a notifier (email or sms)
    notifier = NotifierFactory.create("email")

    # Create the library with the notifier
    library = Library(notifier)

    # Create librarian and two members
    librarian = PersonFactory.create_person("librarian", "Ada", "ada@library.com")
    member1 = PersonFactory.create_person("member", "Tunde", "tunde@email.com")
    member2 = PersonFactory.create_person("member", "Zainab", "zainab@email.com")

    # Librarian adds books
    book1 = Book("Things Fall Apart", "Chinua Achebe", "ISBN001")
    book2 = Book("Half of a Yellow Sun", "Chimamanda Ngozi Adichie", "ISBN002")
    book3 = Book("The Famished Road", "Ben Okri", "ISBN003")
    librarian.add_book(library, book1)
    librarian.add_book(library, book2)
    librarian.add_book(library, book3)

    # Librarian registers both members
    librarian.register_member(library, member1)
    librarian.register_member(library, member2)

    # Members borrow books
    member1.borrow_book(library, "ISBN001")
    member2.borrow_book(library, "ISBN002")
    member1.borrow_book(library, "ISBN002")  # Attempt to borrow unavailable book
    member1.return_book(library, "ISBN001")
    
    # Show current loans for each member
    print("\nTunde's Loans:")
    for book in library.member_loans(member1):
        print("-", book)

    print("\nZainab's Loans:")
    for book in library.member_loans(member2):
        print("-", book)

    # Members return books
    member1.return_book(library, "ISBN001")
    member2.return_book(library, "ISBN002")

    # Show updated loans
    print("\nUpdated Loans After Returns:")
    print("Tunde:", library.member_loans(member1))
    print("Zainab:", library.member_loans(member2))

if __name__ == "__main__":
    main()
