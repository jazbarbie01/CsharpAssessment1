import typing

class Book:
    """Represents a book with a title and genre."""

    ALLOWED_GENRES: typing.Set[str] = {'Teen', 'Drama', 'Sci-Fi', 'Adventure', 'Comedy'}

    def __init__(self, title: str, genre: str):
        """
        Initializes a Book object.

        Args:
            title: The title of the book.
            genre: The genre of the book. Must be one of ALLOWED_GENRES.

        Raises:
            ValueError: If the provided genre is not in ALLOWED_GENRES.
        """
        if genre not in self.ALLOWED_GENRES:
            raise ValueError(f"Genre '{genre}' is not allowed. Allowed genres: {self.ALLOWED_GENRES}")
        self.title = title
        self.genre = genre

    def __repr__(self) -> str:
        """Returns a string representation of the Book object."""
        return f"Book(title='{self.title}', genre='{self.genre}')"
