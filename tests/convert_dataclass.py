from __future__ import annotations

from pydantic.dataclasses import dataclass, Field

from PythonWithPython import *

"""
Convert a Python dataclass into PythonWithPython syntax
"""


@dataclass
class Book:
    title: str
    author: str
    published_year: int = Field(default=2022)

    def is_classic(self) -> bool:
        return self.published_year < 1970

    def update_title(self, new_title: str) -> None:
        self.title = new_title


recreated_book_class = recreate_class(Book)
pwp_code = recreated_book_class.preview()
print(pwp_code)
# recreated_book_class.render() should return Python code that looks exactly like the Book dataclass defined above
original_dataclass = recreated_book_class.render()
print(original_dataclass)

