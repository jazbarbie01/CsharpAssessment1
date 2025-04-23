from library import add_book, view_books, delete_book
from book import Book # Import Book to access ALLOWED_GENRES

def print_menu():
    """Prints the main menu options to the console."""
    print("\n--- Library Menu ---")
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Delete a Book")
    print("4. Exit")
    print("--------------------")

def main():
    """Runs the main application loop for the library."""
    print("Welcome to the Library Management System!")

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            title = input("Enter the book title: ")
            # Display allowed genres to the user
            print(f"Allowed genres are: {', '.join(sorted(Book.ALLOWED_GENRES))}")
            genre = input("Enter the book genre: ")
            add_book(title, genre) # library.add_book handles printing success/error messages
        elif choice == '2':
            view_books() # library.view_books handles printing the list
        elif choice == '3':
            title = input("Enter the title of the book to delete: ")
            delete_book(title) # library.delete_book handles printing success/error messages
        elif choice == '4':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
