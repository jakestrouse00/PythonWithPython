from __future__ import annotations

from types import NoneType

from pydantic.dataclasses import Field, dataclass
from typing import *
from PythonWithPython import *




class_obj = PythonClass("User", [PythonArgument("name", str), PythonArgument("age", int),
                                 PythonArgument("employed", bool, default=PythonField(default=False))],
                        [PythonFunction("is_legal", [], ["return self.age > 18"], bool, in_class=True),
                         PythonFunction("can_employ", [], ["return not self.employed and self.is_legal()"], bool,
                                        in_class=True)])
# print(class_obj.render())

product = PythonClass("Product", [
    PythonArgument("id", int),
    PythonArgument("name", str),
    PythonArgument("price", float | int)
], [
                PythonFunction("is_expensive", [], ["return self.price > 1000.00"], bool, in_class=True),
                PythonFunction("apply_discount", [PythonArgument("discount", float)], ["self.price -= discount"], None,
                               in_class=True)
            ])


# print(product.render())


