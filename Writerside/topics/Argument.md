# Argument

## PythonArgument Class
The PythonArgument class provides a way to programmatically generate Python function or class arguments with type hints and default values. It is particularly useful for code generation tasks, such as dynamically creating functions or classes with specified signatures.

### Overview
The PythonArgument class allows you to define an argument's name, type hint, and default value. It includes methods to render the argument as a string suitable for inclusion in a function or class definition, with optional indentation for formatting.

### Key Features
- **name**: The argument's name as a string.
- **type_hint**: Supports single types or a list of types (which are converted into a Union).
- **default**: Optional default value, which can be a simple value or a custom PythonField instance.

### Usage
#### Creating an Argument
```python
from PythonWithPython import PythonArgument, PythonField
arg = PythonArgument(
    name='x',
    type_hint=int,
    default=PythonField(default=0)
)
```

#### Rendering the Argument
Use the `render` method to generate the code representation of the argument.
```python
argument_code = arg.render(render_type='function')
print(argument_code)

```

