# Class

## PythonClass Class
The PythonClass class enables the dynamic creation and rendering of Python classes, including arguments, inheritance, and methods. It is designed to assist in generating class structures programmatically, especially useful for code generation tasks where class blueprints need to be dynamically constructed.

### Overview
The PythonClass class takes in a class name, arguments (in the form of PythonArgument objects), methods (as PythonFunction objects), and optional inheritance from another class. It provides methods to render the class as Python code, create a Pydantic model from the class, and preview its structure.

### Key Features
* **name**: The name of the class as a string.
* **arguments**: A list of PythonArgument instances representing the class's attributes.
* **functions**: A list of PythonFunction instances representing the class's methods.
* **inherits**: Optional inheritance from a parent class.
### Methods
* **render**: Generates the Python code for the class, including the @dataclass decorator, attributes, and methods, with optional indentation for formatting.
* **create_model**: Creates a Pydantic model of the class based on its attributes.
* **preview**: Provides a string preview of the class structure, useful for debugging and quick inspection.

### Usage

#### Creating a Python Class
```python
from PythonWithPython import PythonClass, PythonArgument, PythonFunction

# Define class arguments and methods
arg1 = PythonArgument(name='id', type_hint=int)
arg2 = PythonArgument(name='name', type_hint=str)
func = PythonFunction(name='get_name', return_type=str, body='return self.name')

# Create a Python class dynamically
my_class = PythonClass(
    name='Person',
    arguments=[arg1, arg2],
    functions=[func]
)

```
#### Rendering the Class
Use the render method to generate Python code for the class.
```python
class_code = my_class.render()
print(class_code)
```