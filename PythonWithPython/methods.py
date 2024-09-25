from __future__ import annotations

from pydantic.dataclasses import Field, dataclass

from .utils import tab_spacing

__all__ = ['PythonMethods']


@dataclass
class PythonMethods:
    static_method: bool = Field(default=False)
    class_method: bool = Field(default=False)
    property_method: bool = Field(default=False)

    def __post_init__(self):
        true_count = sum([self.static_method, self.class_method, self.property_method])
        if true_count > 1:
            raise ValueError("A function cannot have multiple methods at once")

    def render(self, indent: int = 0):
        if indent > 0:
            indent_str = tab_spacing * indent
        else:
            indent_str = ""
        if not self.class_method and not self.static_method and not self.property_method:
            return ""
        output_str = ""
        if self.class_method:
            output_str = f"{indent_str}@classmethod\n"
        if self.static_method:
            output_str = f"{indent_str}@staticmethod\n"
        if self.property_method:
            output_str = f"{indent_str}@property\n"
        return output_str
