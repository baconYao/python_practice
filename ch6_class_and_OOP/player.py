 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import shlex

class Player(object):
    def __init__(self, location):
        self.location = location
        self.location.here.append(self)
        self.name = "Player"
        self.description = "The Player"
        # print self
        # print self.location.here
        self.playing = True
        self.inventory = []
        self.hit_points = 3

    def get_input(self):
        print ""
        return raw_input(">")

    def process_input(self, input):
        """
            shlex.split() to split your command because it handles quotes much better than the normal split
            For example, the player types GET “GOLD KEY,” then shlex.split() will read GOLD KEY as one part. You join anything after the verb and assume it’s part of the noun, so GET GOLD KEY will work, too.
        """
        parts = shlex.split(input)
        if len(parts) == 0:
            return []
        if len(parts) == 1:
            parts.append("")
        verb = parts[0]
        noun = " ".join(parts[1:])

        handler = self.find_handler(verb, noun)
        if handler is None:
            return [input + "? I don't know how to do that!"]
        return handler(self, noun)

    # player's action
    actions = ['quit', 'inv', 'get', 'drop']

    # Exit game
    def quit(self, player, noun):
        self.playing = False
        return ["bye bye!"]
    
    # Get item error handler
    def get(self, player, noun):
        return [noun + "? I can't see that here"]

    # Drop item error handler
    def drop(self, player, noun):
        return [noun + "? I don't have that!"]

    # Check player's inventory list
    def inv(self, player, noun):
        result = ["You have:"]
        if self.inventory:
            result += [x.name for x in self.inventory]
        else:
            result += ["nothing! OPZ"]
        return result

    # Try to find a method to handle it
    def find_handler(self, verb, noun):
        if noun != "":
            # A list to store obejct
            object = [x for x in self.location.here + self.inventory if x is not self and x.name == noun and verb in x.actions]
            if len(object) > 0:
                return getattr(object[0], verb)
        if verb.lower() in self.actions:
            return getattr(self, verb)
        elif verb.lower() in self.location.actions:
            return getattr(self.location, verb)
    
    def attack(self, player, noun):
        if player == self:
            return ["You can't attack yourself"]
        hit_chance = 2
        has_sword = [i for i in player.inventory if i.name == 'sword']
        if has_sword:
            hit_chance += 2
        roll = random.choice([1,2,3,4,5,6])
        if roll > hit_chance:
            self.events.append("The " + player.name + " misses you!")
            return ["You miss the " + self.name]

        self.hit_points -= 1
        if self.hit_points <= 0:
            return_value = ["You kill the " + self.name]
            self.events.append("The " + player.name + " has killed you!")
            self.died()
            return return_value

        self.events.append("The " + player.name + " hits you!")
        return ["You hit the " + self.name]

    def die(self):
        self.playing = False
        self.input = ""
        self.name = "A dead " + self.name


    def update(self):
        self.result = self.process_input(self.input)

    
if __name__ == '__main__':
    import cave
    caves = cave.create_caves()
    # print caves
    cave1 = caves[0]

    import item
    # Initial some treasures
    sword = item.Item("sword", "A point sword.", cave1)
    coin = item.Item("coin", "A shiny gold coin. Your first piece of treasure!", cave1)

    player = Player(cave1)

    print '\n'.join(player.location.look(player, ''))

    # print player.location.name
    # print player.location.description
    # print empty_cave.look(player, "")

    while player.playing:
        input = player.get_input()
        result = player.process_input(input)
        print "\n".join(result)
