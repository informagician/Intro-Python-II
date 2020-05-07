from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     []),

    'foyer':    Room("Foyer", 
                    """Dim light filters in from the south. Dusty passages run north and east.""",
                    ['sword']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",['coin']),
}

# Declare all items

# coin = Item('coin','gold coins')


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# print(room['outside'])
# selection = input('Which direction do you want to go?')

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'])
print(f'You are located at:\n{player.loc.name}\n{player.loc.description}')
player.loc.itemsInRoom()

# possible = {'n': room['outside'].n_to,'e':'e_to','s':'s_to','w':'w_to'}

# print(possible[selection])
# print(player.loc)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# while selection != 'q':
#     print(room[player.loc])
#     selection = input('Which direction do you want to go?')

#     if room[player.loc].go(selection) != False:
#         player.loc = room[player.loc].go(selection)
#         print(player.loc)
#     else:
#         print('There is no room in that direction!')

verb = None
obj = None

while True:
    #print(f'You are located at:\n{player.loc.name}\n{player.loc.description}')
    selection = input('What do you want to do?')
    
    if len(selection.split(' ')) > 1:
        cmd = selection.split(' ')
        verb = cmd[0]
        obj = cmd[1]

    if selection == 'q':
        break
    elif selection == 'n':
        if player.loc.n_to != None:
            player.loc = player.loc.n_to
            print(f'You are located at:\n{player.loc.name}\n{player.loc.description}')
            player.loc.itemsInRoom()
        else:
            print('No rooms in that direction')
    elif selection == 'e':
        if player.loc.e_to != None:
            player.loc = player.loc.e_to
            print(f'You are located at:\n{player.loc.name}\n{player.loc.description}')
            player.loc.itemsInRoom()
        else:
            print('No rooms in that direction')
    elif selection == 's':
        if player.loc.s_to != None:
            player.loc = player.loc.s_to
            print(f'You are located at:\n{player.loc.name}\n{player.loc.description}')
            player.loc.itemsInRoom()
        else:
            print('No rooms in that direction')
    elif selection == 'w':
        if player.loc.w_to != None:
            player.loc = player.loc.w_to
            print(f'You are located at:\n{player.loc.name}\n{player.loc.description}')
            player.loc.itemsInRoom()
        else:
            print('No rooms in that direction')
    elif selection == 'i':
        player.inventory()
    elif verb == 'get':
        if obj in player.loc.items:
            player.take(obj)
            player.loc.items.remove(obj)
        else:
            print('Object not found in this room')
    elif verb == 'drop':
        player.drop(obj)
        player.loc.items.append(obj)
    else:
        print("That is not a valid direction!")