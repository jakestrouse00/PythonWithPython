from __future__ import annotations

import inspect
from dataclasses import fields
from typing import *

from pydantic.dataclasses import is_pydantic_dataclass
from pydantic.fields import FieldInfo, _Unset

from .arguments import PythonArgument
from .classes import PythonClass
from .code import PythonCode
from .fields import PythonField
from .functions import PythonFunction

__all__ = ['recreate_class']


def parse_default_value(field) -> Any:
    if isinstance(field.default, FieldInfo):
        result_dict = {}
        for key_value in field.default.__str__().split(" "):
            split_value = key_value.split('=')
            try:
                result_dict[split_value[0]] = eval(split_value[1])
            except NameError:
                result_dict[split_value[0]] = ForwardRef(split_value[1])

        if "annotation" in result_dict:
            result_dict.pop("annotation")

        return PythonField(**result_dict)
    if "_MISSING_TYPE" in field.default.__repr__():
        return _Unset
    if "_MISSING_TYPE" in field.default_factory.__repr__():
        return _Unset

    return field.default


def parse_arguments(cls) -> List[PythonArgument]:
    args = []
    for field in fields(cls):
        default = parse_default_value(field)
        args.append(
            PythonArgument(name=field.name, type_hint=field.type, default=default)
        )
    return args


def parse_functions(cls) -> List[PythonFunction]:
    functions = []
    for name, method in inspect.getmembers(cls, predicate=inspect.isfunction):

        if not method.__name__.startswith("__"):
            signature = inspect.signature(method)
            parameters = list(filter(lambda x: x is not None, [PythonArgument(name=param.name, type_hint=(
                param.annotation if param.annotation is not param.empty else "")) if param.name != "self" else None for
                                                               param in
                                                               signature.parameters.values()]))

            return_type = signature.return_annotation.replace("'", "")
            # if return_type is

            source_lines = inspect.getsourcelines(method)[0]
            # print(source_lines)
            body = [
                       PythonCode(content=line if "#" not in line else line.split("#")[0].strip(),
                                  comment=line.split("#")[1].strip() if "#" in line else None)
                       for line in source_lines
                   ][1:]  # Skip the function definition line
            functions.append(
                PythonFunction(name=name, arguments=parameters, body=body, return_type=return_type, in_class=True)
            )
    return functions


def recreate_class(cls) -> PythonClass:
    if not is_pydantic_dataclass(cls):
        raise ValueError("The class must be decorated with @dataclass")

    class_name = cls.__name__
    arguments = parse_arguments(cls)
    functions = parse_functions(cls)
    base_classes = [base.__name__ for base in cls.__bases__ if base.__name__ != 'object']

    python_class = PythonClass(
        name=class_name,
        arguments=arguments,
        functions=functions,
    )

    return python_class
