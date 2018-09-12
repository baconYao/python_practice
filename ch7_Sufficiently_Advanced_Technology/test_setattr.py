 #!/usr/bin/python
 # -*- coding: utf-8 -*-

"""
    __getattr__ is used to provide methods or attributes when they’re not found in the class or a parent class. You can use this to catch missing methods or write wrappers around other classes or programs. The following listing shows how you can use the __getattr__ method to override the way Python looks up missing attributes
"""

class TestSetAttr(object):
    def __init__(self):
        # Set up replacement dictionary called "things", which will store all  the attributes you'll set
        self.__dict__['things'] = {}
    
    # __setattr__ insert into tings
    def __setattr__(self, name, value):
        print "Setting '%s' to '%s'" % (name, value)
        self.things[name] = value

    # __getattr__ read from things
    def __getattr__(self, name):
        try:
            return self.things[name]
        except:
            raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, name))
            

test_class = TestSetAttr()
test_class.something = 42

print test_class.something
print test_class.things
print test_class.something_else