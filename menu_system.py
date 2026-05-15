from library import Library
from book import Book
lib = Library()
def menu():
    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Display Available Books")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            book = Book(title, author)
            lib.add_book(book)
        elif choice == "2":
            title = input("Enter book title to issue: ")
            lib.issue_book(title)
        elif choice == "3":
            title = input("Enter book title to return: ")
            lib.return_book(title)
        elif choice == "4":
            lib.display_books()
        elif choice == "5":
            print("Exiting Library System...")
            break
        else:
            print("Invalid choice! Please try again.")
menu()