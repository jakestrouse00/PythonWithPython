from __future__ import annotations

from dataclasses import field
from types import *
from typing import *

import typing_extensions
from pydantic import AliasChoices, AliasPath, Discriminator, PydanticUndefinedAnnotation
from pydantic.dataclasses import dataclass, Field, FieldInfo
from pydantic.fields import Deprecated, JsonDict, _EmptyKwargs, _Unset
from pydantic.v1.config import inherit_config
from pydantic.v1.schema import field_schema
from pydantic_core import PydanticUndefined, PydanticUndefinedType
import annotated_types
from .fields import PythonField
from .utils import tab_spacing

__all__ = ["PythonArgument"]




class PythonArgument:
    def __init__(self, name: str, type_hint: Type | List[Type], default: PythonField | _Unset = _Unset):
        self.name = name
        self.type_hint = type_hint

        self.default = default
        if isinstance(self.default, str):
            self.default = f'"{self.default}"'

        if isinstance(self.type_hint, list):
            self.type_hint = Union[tuple(self.type_hint)]

    def render(self, render_type: Literal['class', 'function'], indent: int = 0):
        if indent > 0:
            indent_str = tab_spacing * indent
        else:
            indent_str = ""
        # print(isinstance(self.default, PydanticUndefinedType))
        # print(self.default)
        if isinstance(self.default, PythonField):
            field_str = self.default.render()

        elif isinstance(self.default, PydanticUndefinedType):
            field_str = ""

        else:
            field_str = f" = {self.default}"

        if isinstance(self.type_hint, UnionType):
            type_hint_name = self.type_hint.__repr__()
        elif isinstance(self.type_hint, str):
            type_hint_name = self.type_hint
        elif isinstance(self.type_hint, type):
            type_hint_name = self.type_hint.__name__
        else:
            type_hint_name = repr(self.type_hint).replace("typing.", "").replace("ForwardRef('", "").replace("')", "").replace("PythonWithPython.classes.", "")
        if render_type == "class":
            return f"{indent_str}{self.name}: {type_hint_name}{field_str}"
        else:
            return f"{indent_str}{self.name}: {type_hint_name}{field_str}"

    def preview(self):
        if isinstance(self.default, PydanticUndefinedType):
            default = ""
        else:
            default = f", default={self.default}"
        return f"PythonArgument(name='{self.name}', type_hint={self.type_hint}{default})"