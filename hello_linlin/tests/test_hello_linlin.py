"""Tests of graph kernels.
"""

import pytest

##############################################################################

def test_hello_linlin():
	"""
	"""
	from hello_linlin import hello_linlin
	hello_linlin()


##############################################################################

def test_hello_linlin_cython():
	"""
	"""
	from hello_linlin import hello_linlin_cython
	hello_linlin_cython()

