from random import choice

cave_numbers = range(1,21)
wumpus_location = choice(cave_numbers)
wumpus_friends_location = choice(cave_numbers)
player_location = choice(cave_numbers)

while (player_location == wumpus_location or player_location == wumpus_friends_location):
    player_location = choice(cave_numbers)

print "Welcome to Hunt the Wumpus!"
print "You can see", len(cave_numbers), "caves" 
print "To play, just type the number"
print "of the cave you wish to enter next"

while True:
    print "You are in cave", player_location
    if (player_location == wumpus_location - 1 or player_location == wumpus_location + 1):
        print "I smell a wumpus!"
    if (player_location == wumpus_friends_location - 1 or player_location == wumpus_friends_location + 1):
        print "I smell an even stinkier wumpus!"
    print "Which cave next?"
    player_input = raw_input(">")
    if (not player_input.isdigit() or int(player_input) not in cave_numbers):
        print player_input, "is not a cave!"
    else:
        player_location = int(player_input)
        if player_location == wumpus_location:
            print "Aargh! You got eaten by a  wumpus!"
            break
        if player_location == wumpus_friends_location:
            print "Aargh! You got eaten by the wumpus' friend"
            break