from __future__ import annotations

from dataclasses import field
from types import *
from typing import *

import typing_extensions
from pydantic import AliasChoices, AliasPath, Discriminator, create_model
from pydantic.dataclasses import dataclass, Field, FieldInfo
from pydantic.fields import Deprecated, JsonDict, _EmptyKwargs, _Unset
from pydantic.v1.config import inherit_config
from pydantic.v1.schema import field_schema
from pydantic_core import PydanticUndefined
import annotated_types
from .arguments import PythonArgument
from .functions import PythonFunction, PythonMethods
from .fields import PythonField
from .utils import tab_spacing

__all__ = ["PythonClass"]


class PythonClass:
    def __init__(self, name: str, arguments: List[PythonArgument], functions: List[PythonFunction],
                 inherits: Type | None = None):
        self.name = name
        self.arguments = arguments
        self.inherits = inherits
        self.functions = functions

    def render(self, indent: int = 0):
        if indent > 0:
            indent_str = tab_spacing * indent
        else:
            indent_str = ""

        if self.inherits is not None:
            inherits_str = f"({self.inherits.__name__})"
        else:
            inherits_str = ""

        output_str = f"{indent_str}@dataclass\n{indent_str}{inherits_str}class {self.name}{inherits_str}:"
        for argument in self.arguments:
            output_str += f"\n{argument.render(render_type='class', indent=indent + 1)}"
        output_str += "\n"
        for function in self.functions:
            output_str += f"\n{function.render(indent=indent + 1)}"
        return output_str

    def create_model(self):
        args = {}
        for argument in self.arguments:
            args[argument.name] = (argument.type_hint, ...)
        return create_model(self.name, **args)

    def preview(self):
        return f"PythonClass(name='{self.name}', arguments=[{', '.join([arg.preview() for arg in self.arguments])}], inherits={self.inherits}, functions=[{', '.join([func.preview() for func in self.functions])}])"







