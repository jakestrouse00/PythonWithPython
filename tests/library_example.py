from __future__ import annotations

from typing import *

from PythonWithPython import *

book = PythonClass("Book", [
    PythonArgument("title", str),
    PythonArgument("author", str),
    PythonArgument("published_year", int)
], [
                       PythonFunction("is_classic", [], ["return self.published_year < 1970"], bool, in_class=True),
                       PythonFunction("update_title", [PythonArgument("new_title", str)], ["self.title = new_title"],
                                      None,
                                      in_class=True)
                   ])

Book = book.create_model()
library = PythonClass("Library", [
    PythonArgument("name", str),
    PythonArgument("books", List[Book], default=PythonField(default_factory=list))
], [
                          PythonFunction("add_book", [PythonArgument("book", Book)], ["self.books.append(book)"], None,
                                         in_class=True),
                          PythonFunction("find_books_by_author", [PythonArgument("author", str)],
                                         [PythonCode("return [book for book in self.books if book.author == author]")],
                                         List[Book],
                                         in_class=True),
                          PythonFunction("list_all_titles", [],
                                         ["return [book.title for book in self.books]"], List[str], in_class=True)
                      ])

print(book.render())
print(library.render())
