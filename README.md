from tests.convert_dataclass import pwp_code

# PythonWithPython

The PythonWithPython is designed for programmatically generating Python code. PythonWithPython provides classes and utilities to define and structure Python code elements like classes, functions, arguments, fields, and methods. It also supports rendering these components into Python code and offers features to recreate Python class structures dynamically.
## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Modules](#modules)
    - [Module 1](#module-1)
    - [Module 2](#module-2)
4. [Contributing](#contributing)
5. [License](#license)

## Installation

To install `PythonWithPython`, use pip:

```bash
pip install git+https://github.com/jakestrouse00/PythonWithPython.git@main
```

## Overview
The package is structured to allow users to create Python classes, functions, and methods in a modular fashion. It includes the following key components:

- **PythonClass**: Represents a Python class with attributes, methods, and optional inheritance.
- **PythonFunction**: Represents Python functions with support for arguments and rendering.
- **PythonMethods**: Likely an extension or specialization of PythonFunction for class methods.
- **PythonArgument**: Represents the arguments passed to functions or classes.
- **PythonField**: Represents the fields or attributes within a class.

#### Helper functions
- **recreate_class()**: Convert class in Python to PythonWithPython syntax

## Main Classes
### `PythonClass`
- **Purpose**: Defines a Python class, including its name, arguments (attributes), methods (functions), and inheritance.
- **Key Methods**:
  - **render(indent=0)**: Generates a string representation of the class in PWP syntax, including the class signature and body, with optional indentation.
  - **create_model()**: Uses the pydantic.create_model method to dynamically create a Pydantic model based on the class arguments.
  - **preview()**: Provides a textual preview of the class structure, useful for debugging or inspection.
### `PythonFunction`
- **Purpose**: Defines a Python function, including its name, arguments, and body. It is used for creating class methods or standalone functions.
- **Key Methods**:
  - **render(indent=0)**: Generates a string representation of the function in PWP syntax, including the function signature and body, with optional indentation.
  - **preview()**: Provides a textual preview of the function's PWP syntax, useful for debugging or inspection.
### `PythonArgument`
- **Purpose**: Represents an argument passed to a Python function or class. This includes the argument's name and type hint.
- **Key Methods**:
  - **render(indent=0)**: Generates a string representation of the argument in PWP syntax, including the argument typehint and default, with optional indentation.
  - **preview()**: Provides a textual preview of the argument's PWP syntax, useful for debugging or inspection.
## Usage
### Quick Start

#### Basic Syntax

Here's a simple example demonstrating how to use `PythonWithPython`:

Say we wanted to recreate the following dataclass in `PythonWithPython` syntax
```python
from pydantic.dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    published_year: int

    def is_classic(self) -> bool:
        return self.published_year < 1970

    def update_title(self, new_title: str) -> None:
        self.title = new_title
```
To do this you would typically follow these steps:
```python
from PythonWithPython import *

# Define the class arguments
class_arguments = [
    PythonArgument(name='title', type_hint=str),
    PythonArgument(name='author', type_hint=str),
    PythonArgument(name='published_year', type_hint=int)
]

# Define the functions within the class

is_classic_function = PythonFunction(
    name='is_classic',
    arguments=[],
    body=[PythonCode(content='return self.published_year < 1970', comment=None)],
    return_type=bool,
    method=PythonMethods(static_method=False, class_method=False, property_method=False),
    in_class=True
)

update_title_function = PythonFunction(
    name='update_title',
    arguments=[PythonArgument(name='new_title', type_hint=str)],
    body=[PythonCode(content='self.title = new_title', comment=None)],
    return_type=None,
    method=PythonMethods(static_method=False, class_method=False, property_method=False),
    in_class=True
)
# Put it all together
book_class = PythonClass(name='book', arguments=class_arguments, functions=[is_classic_function, update_title_function])

# Verify that everything worked properly
print(book_class.render())
```

Doing all this can be time consuming, so I recommend you check out how to [automatically convert](#auto-convert-python-to-pythonwithpython-syntax) python dataclasses into `PythonWithPython` syntax in the [Extra section](#extra).

#### Advanced Syntax
If you want to use defaults, pydantic.dataclass.Field, or reference one dataclass from another

##### pydantic.dataclass.Field
```python

```



### Extra

#### Auto Convert Python to PythonWithPython Syntax

```python
from pydantic.dataclasses import dataclass
from PythonWithPython import *

# dataclass we want to convert
@dataclass
class Book:
    title: str
    author: str
    published_year: int

    def is_classic(self) -> bool:
        return self.published_year < 1970

    def update_title(self, new_title: str) -> None:
        self.title = new_title

# pass the dataclass into recreate_class() to create a fully formed PythonClass
pwp_code: PythonClass = recreate_class(Book)
# use .preview() to get the PythonWithPython code
# or use .render() to verify the results
print(pwp_code.preview())
```



## License

`PythonWithPython` is released under the MIT License. See the [LICENSE](LICENSE) file for more details.