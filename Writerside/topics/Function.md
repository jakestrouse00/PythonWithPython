# Function

## PythonFunction Class

The `PythonFunction` class provides a way to programmatically generate Python functions with customizable arguments, method decorators, and function bodies. It is particularly useful for code generation tasks, enabling users to dynamically create function definitions with specified signatures and return types.

### Overview

The `PythonFunction` class allows you to define a function's name, arguments, return type, and body. It also supports method decorators, such as `@staticmethod` or `@classmethod`, and can handle indentation formatting for clean code generation.

### Key Features

- **name**: The function's name as a string.
- **arguments**: A list of `PythonArgument` instances representing the function's parameters.
- **body**: A list of strings or `PythonCode` instances representing the function's body.
- **return_type**: The return type of the function, which can be a type, a string, or `None` for no return type.
- **method**: A `PythonMethods` instance, allowing for method decorators like `@staticmethod` or `@classmethod`.
- **in_class**: A boolean indicating whether the function is a method inside a class (affects the inclusion of `self` in the argument list).

### Usage

#### Creating a Function

```python
from PythonWithPython import PythonFunction, PythonArgument, PythonCode

function = PythonFunction(
    name='example_function',
    arguments=[PythonArgument(name='x', type_hint=int, default=0)],
    body=[PythonCode(content='return x * 2')],
    return_type=int
)
```

#### Rendering the Function
Use the render method to generate the code representation of the function.
```python
function_code = function.render()
print(function_code)

```