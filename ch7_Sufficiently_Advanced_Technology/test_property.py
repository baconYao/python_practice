 #!/usr/bin/python
 # -*- coding: utf-8 -*-

"""
    A detailed property introduction
    https://www.programiz.com/python-programming/property
"""

class TestProperty(object):
    def __init__(self, x):
        self.x  = x

    # My getter
    def get_x(self):
        return self._x

    # My setter
    def set_x(self, value):
        if not (type(value) == int and 0 <= value < 32):
            raise ValueError("TestProperty.x must be an integer from 0 to 31")
        self._x = value

    # Define property
    x = property(get_x, set_x)

test = TestProperty(10)
print test.x
test.x = 11
test.x += 1
assert test.x == 12
print test.x

try:
    test2 = TestProperty(42)
except ValueError:
    # ValueError: Testproperty.x must be an integer between 0 and 32
    print "test2 not set to 42"
