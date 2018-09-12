 #!/usr/bin/python
 # -*- coding: utf-8 -*-

"""
    __getattr__ is used to provide methods or attributes when they’re not found in the class or a parent class. You can use this to catch missing methods or write wrappers around other classes or programs. The following listing shows how you can use the __getattr__ method to override the way Python looks up missing attributes
"""

class TestGetAttr(object):
    
    def __getattr__(self, name):                              
        print "Attribute '%s' not found!" % name
        return 42    

test_class = TestGetAttr()
print test_class.something          # can't find something

test_class.something = 43
print test_class.something          # can find something
