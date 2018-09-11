 #!/usr/bin/python
 # -*- coding: utf-8 -*-

class Item(object): 
    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.location = location
        self.location.here.append(self)

    actions = ['look', 'get', 'drop']

    """
        When the player issues a LOOK ITEM command with the item’s name as a noun, this is the method that will be called; all it does is return the item’s description.
    """
    def look(self, player, noun):
        return [self.description]

    # Get item method
    def get(self, player, noun):
        # Check whether already added
        if self.location is player:
            return ["You already have the " + self.name]
        # Remove item from here
        self.location.here.remove(self)
        # Add item to player's location (means item will follow the player goes to everywhere)
        self.location = player
        # Add item to player's inventory
        player.inventory.append(self)
        return ["You get the " + self.name]

    # Drop item method
    def drop(self, player, noun):
        if self not in player.inventory:
            return ["You don't have the " + self.name]
        # Remove item from inventory
        player.inventory.remove(self)
        # Drop item to the where player is now
        player.location.here.append(self)
        # Assign item's location same as player location now
        self.location = player.location
        return ["You drop the " + self.name]
