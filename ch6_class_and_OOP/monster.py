import random
import player

class Monster(player.Player):
    def __init__(self, location, name, description):
        # Call parent classes __init__
        player.Player.__init__(self, location)
        self.name = name
        self.description = description

    # Monster's brain
    def get_input(self):            # Monster dosen't know it's dead
        if not self.playing:
            return ""
        player_present = [x for x in self.location.here if x.name == "Player"]
        if player_present:
            return "attack " + player_present[0].name
        if random.choice((0, 1)):
            return ("go " + random.choice(self.location.exits()))
        else:
            return ""
    # Functions for player interaction
    def look(self, player, noun):
        return [self.name, self.description]
    def get(self, player, noun):
        return ["The " + self.name + " growls at you."]