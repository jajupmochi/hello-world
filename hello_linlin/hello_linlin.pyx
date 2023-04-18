cdef extern from "hello_linlin.cpp":
    void hello_linlin()

def say_hello():
    hello_linlin()
    print('Hello Linlin from Cython .pyx file!')


# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sat Feb 12 11:51:00 2022
#
# @author: ljia
# """
# def hello_linlin():
# 	print('Hello, Linlin!')
#
#
# def hello_linlin_cython():
# 	print('Hello, Linlin! I am Cython!')
