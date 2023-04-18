cdef extern from "hello.cpp":
    void hello()

def say_hello():
    hello()

