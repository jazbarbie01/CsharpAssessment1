import unittest
import io
import contextlib

# Import classes and functions to be tested
from book import Book
import library # Import the module itself to access the global 'books' list
from library import add_book, delete_book, view_books

class TestLibrary(unittest.TestCase):
    """Test suite for the library management system."""

    def setUp(self):
        """Set up test fixtures, clear the library before each test."""
        # Clear the global books list in the library module
        library.books.clear()
        # Add some initial books directly to the list for a known state
        try:
            library.books.append(Book("Test Book 1", "Sci-Fi"))
            library.books.append(Book("Test Book 2", "Teen"))
            self.initial_book_count = 2
        except ValueError:
            # This shouldn't happen with valid genres, but good practice
            self.fail("setUp failed: Could not add initial books with valid genres.")

    # --- Book Class Tests ---
    def test_book_creation_valid_genre(self):
        """Test creating a Book with a valid genre."""
        try:
            book = Book("Valid Genre Book", "Comedy")
            self.assertEqual(book.title, "Valid Genre Book")
            self.assertEqual(book.genre, "Comedy")
        except ValueError:
            self.fail("Book creation failed unexpectedly with a valid genre.")

    def test_book_creation_invalid_genre(self):
        """Test creating a Book with an invalid genre raises ValueError."""
        with self.assertRaises(ValueError):
            Book("Invalid Genre Book", "Historical")

    # --- Library Function Tests ---
    def test_add_book_success(self):
        """Test adding a new book successfully."""
        result = add_book("New Adventure", "Adventure")
        self.assertTrue(result)
        self.assertEqual(len(library.books), self.initial_book_count + 1)
        # Check if the book details are correct in the list
        self.assertEqual(library.books[-1].title, "New Adventure")
        self.assertEqual(library.books[-1].genre, "Adventure")

    def test_add_book_duplicate_title(self):
        """Test adding a book with a duplicate title (case-insensitive)."""
        result = add_book("test book 1", "Drama") # Case-insensitive duplicate
        self.assertFalse(result)
        self.assertEqual(len(library.books), self.initial_book_count) # Count should not increase

    def test_add_book_invalid_genre(self):
        """Test adding a book with an invalid genre."""
        result = add_book("Invalid Genre Book", "Mystery")
        self.assertFalse(result)
        self.assertEqual(len(library.books), self.initial_book_count) # Count should not increase

    def test_delete_book_success(self):
        """Test deleting an existing book successfully."""
        result = delete_book("Test Book 1")
        self.assertTrue(result)
        self.assertEqual(len(library.books), self.initial_book_count - 1)
        # Verify the correct book was removed
        remaining_titles = [book.title for book in library.books]
        self.assertNotIn("Test Book 1", remaining_titles)
        self.assertIn("Test Book 2", remaining_titles)

    def test_delete_book_not_found(self):
        """Test deleting a book that doesn't exist."""
        result = delete_book("Non Existent Book")
        self.assertFalse(result)
        self.assertEqual(len(library.books), self.initial_book_count) # Count should remain unchanged

    def test_view_books_runs(self):
        """Test that view_books runs without error when library is not empty."""
        # Capture stdout to prevent printing during tests, but don't assert content
        string_io = io.StringIO()
        with contextlib.redirect_stdout(string_io):
            try:
                view_books()
            except Exception as e:
                self.fail(f"view_books() raised an exception when library not empty: {e}")

    def test_view_books_runs_when_empty(self):
        """Test that view_books runs without error when library is empty."""
        library.books.clear() # Ensure library is empty for this test
        string_io = io.StringIO()
        with contextlib.redirect_stdout(string_io):
            try:
                view_books()
            except Exception as e:
                self.fail(f"view_books() raised an exception when library empty: {e}")
        # Optional: Check if the "empty" message is printed
        # self.assertIn("The library is currently empty.", string_io.getvalue())

if __name__ == '__main__':
    unittest.main()
