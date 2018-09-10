 #!/usr/bin/python
 # -*- coding: utf-8 -*-

class Item(object): 
    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.location = location
        location.here.append(self)

    actions = ['look']

    """
        When the player issues a LOOK ITEM command with the item’s name as a noun, this is the method that will be called; all it does is return the item’s description.
    """
    def look(self, player, noun):
        return [self.description]
