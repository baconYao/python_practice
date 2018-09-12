 #!/usr/bin/python
 # -*- coding: utf-8 -*-

class LittleNumber(object):
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

    def __eq__(self, other):
        return self.x == other.x
    
    def __lt__(self, other):
        return self.x < other.x

    def __add__(self, other):
        try:
            if type(other) == int:
                return LittleNumber(self.x + other)
            elif type(other) == LittleNumber:
                return LittleNumber(self.x + other.x)
            else:
                return NotImplemented
        except ValueError:
            raise ValueError("Sum of %d and %d is out of bounds for LittleNumber!" % (self.x, other.x))
    
    def __str__(self):
        return "<LittleNumber: %d>" % self.x


one = LittleNumber(1)
two = LittleNumber(2)
print one == one
print not one == two
print one != two
print one < two
print two > one
print not one > two
print two >= one
print two >= two

onetoo = LittleNumber(1)
print onetoo == one
print not onetoo == two

print onetoo + one
print onetoo
print onetoo + one == two