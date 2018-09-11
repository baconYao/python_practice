 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from random import choice, shuffle

class Cave(object):
    # List of directions and opposite directions
    directions = {
        'north': 'south',
        'east': 'west',
        'south': 'north',
        'west': 'east',
    }

    def __init__(self, name, description):
        self.name = name
        # Descripe the cave when the player enters it
        self.description = description
        # Store any other objects (such as the player, monsters, and treasure) that might be in the cave
        self.here = []
        self.tunnels = {}
        # Add tunnels to cave (Initialize)
        for direction in self.directions.keys():
            self.tunnels[direction] = None

    # Each cave "knows" what it's conneted to
    def tunnel_to(self, direction, cave):
        """ Create a two-way tunnel """
        # Exceptions to handle bad behaviour
        if direction not in self.directions:
            raise ValueError(direction + " is not a valid direction!")
        reverse_direction = self.directions[direction]
        if cave.tunnels[reverse_direction] is not None:
            raise ValueError("Cave " + str(cave) + " already has a cave to the " + reverse_direction + "!")
        # Tunnel from on cave to another
        self.tunnels[direction] = cave
        cave.tunnels[reverse_direction] = self

    def can_tunnel_to(self):
        return [v for v in self.tunnels.values() if v is None] != [] 

    # List all valid exits for a particular cave
    def exits(self):
        return [direction for direction, cave in self.tunnels.items() if cave is not None]
    
    # Look some information
    def look(self, player, noun):
        if noun == "":
            result = [self.name, self.description]
            # Look items
            if len(self.here) > 0:
                result += ["Item here:"]
                result += [x.name for x in self.here if 'name' in dir(x)]
            # Look all exits
            if len(self.exits()) > 0:
                result += ['Exits:']
                for direction in self.exits():
                    result += [direction + ": " + self.tunnels[direction].name]
        else:
            result = [noun + "? I can't see taht."]
        return result

    def go(self, player, noun):
        # Check player input
        if noun not in self.directions:
            return [noun + "? I don't know that direction!"]
        if self.tunnels[noun] is None:
            return ["Can't go " + noun + " from here!"]
        
        # Move
        self.here.remove(player)        # Remove player from this cave
        self.tunnels[noun].here.append(player)          # Add player into the cave which is picked up by player
        player.location = self.tunnels[noun]            # Change player's location
        return (['You go ' + noun] + self.tunnels[noun].look(player, ''))

    # Add some shortcuts
    def north(self, player, noun):
        return self.go(player, 'north')
    n = north

    def east(self, player, noun):
        return self.go(player, 'east')
    e = east

    def south(self, player, noun):
        return self.go(player, 'south')
    s = south

    def west(self, player, noun):
        return self.go(player, 'west')
    w = west
    l = look

    actions = ['look', 'l', 'go', 'north', 'east', 'south', 'west', 'n', 'e', 's', 'w']

    # Add __repr__ method
    """
        The one that’s built in to the base object is a little unreadable (it will be something like <__main__.Cave object at 0x00B38EF0>), and this makes your program’s output look much nicer when you have to print out a cave
        Another resource: https://www.codecademy.com/en/forum_questions/551c137f51b887bbc4001b73
    """
    def __repr__(self):
        return "<Cave " + self.name + ">"


"""
    Assign each one to a new cave instance, link that instance to an existing cave, and then add it into the caves list
"""
def create_caves():
    shuffle(cave_names)
    caves = [Cave(cave_names[0],"")]
    for name in cave_names[1:]:
        new_cave = Cave(name, name)
        # Pick cave from list
        eligible_caves = [cave for cave in caves if cave.can_tunnel_to()]
        old_cave = choice(eligible_caves)
        # Pick Direction to link it to
        directions = [direction for direction, cave in old_cave.tunnels.items() if cave is None]
        direction = choice(directions)
        # Link in new cave
        old_cave.tunnel_to(direction, new_cave)
        caves.append(new_cave)
    return caves



if __name__ == '__main__':
    for cave in create_caves():
        print cave.name, "=>", cave.tunnels