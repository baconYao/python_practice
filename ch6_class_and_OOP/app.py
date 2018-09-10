from random import choice

class Caves(object):
    def __init__(self, number_of_caves):
        self.number_of_caves == number_of_caves
        self.cave_list = range(number_of_caves)
        self.unvisited = range(number_of_caves)[1:]
        self.visited = [0]
        self.caves = []
        self.setup_caves(number_of_caves)
        self.link_caves()

    def setup_caves(self, cave_numbers):
        """ Create the starting list of caves """
        for cave in range(cave_numbers:
            self.caves.append([])