from book import Book
import typing

# Use the allowed genres directly from the Book class
ALLOWED_GENRES = Book.ALLOWED_GENRES

# Initialize the list to store books
books: typing.List[Book] = []

def initialize_library():
    """Adds default books to the library."""
    try:
        books.append(Book("The Hunger Games", "Teen"))
        books.append(Book("Dune", "Sci-Fi"))
        books.append(Book("To Kill a Mockingbird", "Drama")) # Using Drama as an example
    except ValueError as e:
        print(f"Error initializing library with default books: {e}")

# Populate the library initially
initialize_library()

def add_book(title: str, genre: str) -> bool:
    """
    Adds a new book to the library after validation.

    Args:
        title: The title of the book to add.
        genre: The genre of the book to add.

    Returns:
        True if the book was added successfully, False otherwise.
    """
    # Check for duplicate title (case-insensitive)
    for book in books:
        if book.title.lower() == title.lower():
            print(f"Error: Book with title '{title}' already exists.")
            return False

    # Validate genre using Book's validation (implicitly via constructor)
    try:
        new_book = Book(title, genre)
        books.append(new_book)
        print(f"Success: Book '{title}' added to the library.")
        return True
    except ValueError as e:
        # Catch the ValueError raised by Book.__init__ if genre is invalid
        print(f"Error adding book: {e}")
        return False

def view_books():
    """Prints the details of all books in the library."""
    if not books:
        print("The library is currently empty.")
    else:
        print("\n--- Library Collection ---")
        for book in books:
            print(book) # Uses the __repr__ method of Book
        print("------------------------\n")

def delete_book(title: str) -> bool:
    """
    Deletes a book from the library by title.

    Args:
        title: The title of the book to delete.

    Returns:
        True if the book was deleted successfully, False otherwise.
    """
    book_to_delete = None
    for book in books:
        if book.title.lower() == title.lower():
            book_to_delete = book
            break

    if book_to_delete:
        books.remove(book_to_delete)
        print(f"Success: Book '{title}' deleted from the library.")
        return True
    else:
        print(f"Error: Book with title '{title}' not found.")
        return False
