from __future__ import annotations

from pydantic.dataclasses import dataclass

__all__ = ['PythonCode']


@dataclass
class PythonCode:
    content: str
    comment: str | None = None  # Optional comment for the line

    def __post_init__(self):
        if self.comment is None:
            self.comment = ""
        else:
            self.comment = f" # {self.comment}"

        self.content = self.content.replace("\n", "").replace("\t", "").strip()

    def preview(self):
        return f"PythonCode(content={repr(self.content)}, comment={repr(self.comment) if self.comment != '' else None})"
