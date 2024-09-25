from setuptools import setup, find_packages

setup(
    name='PythonWithPython',
    version='1.0.0',
    description='Write Python code with Python!',
    author='Jake Strouse',
    author_email='jstrouse@meh.llc',
    url='https://github.com/jakestrouse00/PythonWithPython',
    packages=find_packages(),
    install_requires=[
        'pydantic'
    ],
)