from __future__ import annotations
from typing import *
from PythonWithPython import *
from pydantic.dataclasses import dataclass, Field

@dataclass
class Book:
    title: str
    author: str
    published_year: int

    def is_classic(self) -> bool:
        return self.published_year < 1970

    def update_title(self, new_title: str) -> None:
        self.title = new_title

@dataclass
class Library:
    name: str
    books: List[Book] = Field(default_factory=list)

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def find_books_by_author(self, author: str) -> List[Book]:
        return [book for book in self.books if book.author == author]

    def list_all_titles(self) -> List[str]:
        return [book.title for book in self.books]


recreated_book_class = recreate_class(Book)
recreated_library_class = recreate_class(Library)

print(recreated_book_class.preview())
print(recreated_library_class.preview())

print(recreated_book_class.render())
print(recreated_library_class.render())