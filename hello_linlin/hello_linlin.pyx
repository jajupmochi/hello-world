cdef extern from "hello_linlin.cpp":
    void hello_linlin()

def say_hello():
    hello_linlin()
    print('Hello Linlin from Cython .pyx file!')
