 #!/usr/bin/python
 # -*- coding: utf-8 -*-
 
"""
    https://stackoverflow.com/questions/3278077/difference-between-getattr-vs-getattribute
"""

class TestGetAttribute(object):
    def __init__(self, things=None):
        # Borrow object's getattribute
        my_dict = object.__getattribute__(self, '__dict__')

        if not things:
            my_dict['things'] = {}
        else:
            my_dict['things'] = things

    def __setattr__(self, name, value):
        print "Setting '%s' to '%s'" % (name, value)
        my_dict = get_real_attr(self, '__dict__')
        my_dict['things'][name] = value

    def __getattribute__(self, name):
        try:
            my_dict = get_real_attr(self, '__dict__')
            return my_dict['things'][name]
        except:
            my_class = get_real_attr(self, '__class__')
            raise AttributeError("'%s' object has no attribute '%s'" % (my_class.__name__, name))

def get_real_attr(instance, name):
    return object.__getattribute__(instance, name)


test = TestGetAttribute({'foo': 'bar'})
print object.__getattribute__(test, '__dict__')
test.something = 43
print object.__getattribute__(test, '__dict__')
print test.foo