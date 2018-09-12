 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import logging          # https://docs.python.org/2/howto/logging.html#logging-basic-tutorial

class Loggable(object):
    """ Mixin class to add logging """
    # Initialize Loggable
    def __init__(self, 
                log_file_name = 'log.txt',
                log_level = logging.INFO,
                log_name = 'MyApp'):
        self.log_file_name = log_file_name
        self.log_level = log_level
        self.log_name = log_name
        self.logger = self._get_logger()

    # Create Logger Object
    def _get_logger(self):
        # Create a logger instance
        logger = logging.getLogger(self.log_name)
        logger.setLevel(self.log_level)
        # Handler
        handler = logging.FileHandler(self.log_file_name)       # FileHandler --> instances send messages to disk files.
        logger.addHandler(handler)
        # How to write out log lines
        formatter = logging.Formatter(
            "%(asctime)s: %(name)s -"
            "%(levelname)s - %(message)s")
        handler.setFormatter(formatter)

        return logger

    # Logging method (log)
    def log(self, log_line, severity=None):
        self.logger.log(severity or self.log_level, log_line)
    # Logging method (warn)
    def warn(self, log_line):
        self.logger.warn(log_line)

class MyClass(Loggable):
    """ A class that you've written """
    def __init__(self):
        # How do you call Loggable.__init__()
        Loggable.__init__(self, log_file_name = 'log2.txt')
        #super(Myclass, self).__init__(log_file_name = 'log2.txt')

    def do_something(self):
        print "Doing something!"
        self.log("I did something")
        self.log("Some debugging info", logging.DEBUG)
        self.warn("Something bad happened!")

test = MyClass()
test.do_something()