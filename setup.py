from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("hello", ["hello.pyx"], language="c++")
]

setup(
    name="hello",
    version="0.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="A demo package that says hello",
    ext_modules=cythonize(extensions)
)

