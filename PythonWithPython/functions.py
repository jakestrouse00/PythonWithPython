from __future__ import annotations

from typing import *

from pydantic.fields import _Unset
from pydantic_core import PydanticUndefinedType

from .arguments import PythonArgument
from .code import PythonCode
from .methods import PythonMethods
from .utils import tab_spacing

__all__ = ["PythonFunction"]


class PythonFunction:
    def __init__(self, name: str, arguments: list[PythonArgument], body: List[str] | List[PythonCode],
                 return_type: Type | _Unset | None = _Unset, method: PythonMethods | None = None,
                 in_class: bool = False):
        if method is None:
            method = PythonMethods()
        self.name = name
        self.arguments = arguments
        self.body = body
        self.method = method
        self.return_type = return_type
        self.in_class = in_class

        new_body = []
        for line in self.body:
            if isinstance(line, str):
                new_body.append(PythonCode(content=line))
            else:
                new_body.append(line)
        self.body = new_body

    def render(self, indent: int = 0):
        if indent > 0:
            indent_str = tab_spacing * indent
        else:
            indent_str = ""
        self.method.render()
        output_str = f"{self.method.render(indent=1)}{indent_str}def {self.name}"
        renders = []
        if self.in_class:
            renders.append("self")
        if not self.method.property_method:
            for argument in self.arguments:
                renders.append(argument.render(render_type='function'))
        # print(renders)
        if isinstance(self.return_type, PydanticUndefinedType):
            return_str = ""

        else:
            if self.return_type is not None:
                if isinstance(self.return_type, type):
                    return_str = f" -> {self.return_type.__name__}"
                else:
                    if isinstance(self.return_type, str):
                        return_str = " -> " + self.return_type.replace("typing.", "").replace("ForwardRef('",
                                                                                              "").replace("')",
                                                                                                          "").replace(
                            "PythonWithPython.classes.", "")

                    else:
                        return_str = " -> " + repr(self.return_type).replace("typing.", "").replace("ForwardRef('",
                                                                                                    "").replace("')",
                                                                                                                "").replace(
                            "PythonWithPython.classes.", "")
            else:
                return_str = " -> None"
        output_str += f"({', '.join(renders)}){return_str}:\n"
        for line in self.body:
            if isinstance(line, PythonCode):
                output_str += f"{indent_str}{tab_spacing}{line.content}{line.comment}\n"
            else:
                output_str += f"{indent_str}{tab_spacing}{line}\n"
        return output_str

    def preview(self):
        return f"PythonFunction(name='{self.name}', arguments=[{', '.join([arg.preview() for arg in self.arguments])}], body=[{', '.join([line.preview() for line in self.body])}], return_type={self.return_type}, method={self.method if self.method is not None else None}, in_class={self.in_class})"
