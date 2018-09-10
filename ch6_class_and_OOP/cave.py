 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from random import choice, shuffle

class Cave(object):
    def __init__(self, name, description):
        self.name = name
        # Descripe the cave when the player enters it
        self.description = description
        # Store any other objects (such as the player, monsters, and treasure) that might be in the cave
        self.here = []
        self.tunnels = []

    # Each cave "knows" what it's conneted to
    def tunnel_to(self, cave):
        """ Create a two-way tunnel """
        # self is the current Cave instance
        self.tunnels.append(cave)
        cave.tunnels.append(self)

    # Add __repr__ method
    """
        The one that’s built in to the base object is a little unreadable (it will be something like <__main__.Cave object at 0x00B38EF0>), and this makes your program’s output look much nicer when you have to print out a cave
        Another resource: https://www.codecademy.com/en/forum_questions/551c137f51b887bbc4001b73
    """
    def __repr__(self):
        return "<Cave " + self.name + ">"

cave_names = [
    "Arched cavern",
    "Twisty passages",
    "Dripping cave",
    "Dusty crawlspace",
    "Underground lake",
    "Black pit",
    "Fallen cave",
    "Shallow pool",
    "Icy underground river",
    "Sandy hollow",
    "Old firepit",
    "Tree root cave",
    "Narrow ledge",
    "Winding steps",
    "Echoing chamber",
    "Musty cave",
    "Gloomy cave",
    "Low ceilinged cave",
    "Wumpus lair",
    "Spooky Chasm",
]

"""
    Assign each one to a new cave instance, link that instance to an existing cave, and then add it into the caves list
"""
def create_caves():
    shuffle(cave_names)
    caves = [Cave(cave_names[0],"")]
    for name in cave_names[1:]:
        new_cave = Cave(name, name)
        eligible_caves = [cave for cave in caves if len(cave.tunnels) < 3]
        new_cave.tunnel_to(choice(eligible_caves))
        caves.append(new_cave)
    return caves

if __name__ == '__main__':
    for cave in create_caves():
        print cave.name, "=>", cave.tunnels