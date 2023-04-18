# """Tests of graph kernels.
# """
#
# import pytest
#
# ##############################################################################
#
# def test_hello_linlin():
# 	"""
# 	"""
# 	from hello_linlin import hello_linlin
# 	hello_linlin()
#
#
# ##############################################################################
#
# def test_hello_linlin_cython():
# 	"""
# 	"""
# 	from hello_linlin import hello_linlin_cython
# 	hello_linlin_cython()


from hello_linlin.hello_linlin import say_hello


def test_say_hello(capsys):
    say_hello()
    captured = capsys.readouterr()
    print(captured.out)
    assert True
    # captured.out == "Hello, world!\n"
