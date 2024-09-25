# Methods

## PythonMethods Class
The `PythonMethods` class provides an easy way to define and manage method decorators for Python functions, specifically handling `@staticmethod`, `@classmethod`, and `@property`. This class ensures that only one method decorator can be applied to a function at a time, raising an error if multiple decorators are attempted.

### Overview
The `PythonMethods` class allows you to define whether a function is a static method, class method, or property. It provides a convenient method to render the appropriate decorator as a string for inclusion in dynamically generated code.

### Key Features
- **static_method**: A boolean flag indicating if the method is a `@staticmethod`.
- **class_method**: A boolean flag indicating if the method is a `@classmethod`.
- **property_method**: A boolean flag indicating if the method is a `@property`.
- **render()**: Generates the appropriate decorator as a string, with optional indentation.

### Usage

#### Creating a PythonMethods instance
```python
from PythonWithPython import PythonMethods

# Create a PythonMethods instance for a static method
method_decorator = PythonMethods(static_method=True)

# Create a PythonMethods instance for a class method
method_decorator = PythonMethods(class_method=True)

# Create a PythonMethods instance for a property
method_decorator = PythonMethods(property_method=True)

```
#### Rendering the Method Decorator
Use the render method to generate the appropriate decorator for the method, optionally providing an indentation level for formatting.
```python
method_code = method_decorator.render(indent=1)
print(method_code)
# Output: "    @staticmethod\n"

```
