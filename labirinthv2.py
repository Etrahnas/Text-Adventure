import pygame
from sys import exit


def get_help():
    """When called, it will display the instructions.
    """
    print()
    print("--------------------------------------------------------------")
    print("How to play:")
    print("\tUse directional commands to navigate the map: 'north', 'south', 'east' and 'west'.")
    print("\tType 'inventory' to check the items you have")
    print("\tThe 'take' command lets you pick up items and the 'use' command to... well, use them.")
    print("\t\tFor example: 'take axe' will pick up the axe and 'use axe' will use the axe on the current area.")
    print("\tFortunately, you have a map of the area, it is displayed in a separate window...")
    print("...please note: if you close the window, the program in the terminal also terminates.")
    print("\tTo recap the controls, type 'help'.")
    print("\tFinally, 'quit' will exit the game.")
    print("--------------------------------------------------------------")
    print()   


# ----------------------
# ---Area definitions---
#-----------------------
# These lists represent the areas of the game. List indexes are: ID, name, description, items to be found hints,
# items to be used, open/closed switch, item using tips, items in area. Exits are stored in a separate adjacancy list.
# Items to find: list with two elements. First element is used when the item is not aquired yet and second when we already picked it up.
# item using tips: Displayed until the right item is used. 

forest_start = [
    1,
    "North forest entrance",
    """
    You are in the north side of the forest. No clouds in the sky, the sun is so bright.
This is such a nice day for an adventure.
Nothing interesting here, so you decide to move along.
There is a long road to the 'east' and a path to the 'south' that leads to a junction.
    """,
    [],
    [],
    False,
    [],
    [],
]
forest_junction = [
    2,
    "Forest junction",
    """
    You are at a junktion. You can go back to the northern area to the 'north', you can
    investigate a large clearence to the 'west', or the ruins to 'east'.
    You look around but noting interesting here.
    """,
    [],
    [],
    False,
    [],
    [],
]
western_ruins = [
    3,
    "Western ruins",
    """
    The path leads you to a large clearence. You see some kind of old ruins here. You wonder,
    what the purpose of this place was centuries ago.
    You can go 'east' to the forest junction, or to the 'west', deep in the forest.
    """,
    ["There is a rotten half-opened chest here. You see a 'sword' within.", "The chest is empty."],
    [],
    False,
    [],
    ["sword"],
]
west_forest = [
    4,
    "Western deep forest",
    """
    You are deep in the forest. The place is dark and you see trees everywhere. Kind of disturbing.
    To the 'east', you can see the Western ruins in the distance.
    A long path goes to the 'south', along the castle walls. It should lead to the main entrance.
    Nothing interesting here to take.
    """,
    [],
    [],
    False,
    [],
    [],
]
eastern_ruins = [
    5,
    "Eastern forest ruins",
    """
    There are multiple columns sorrounding the clearing. This must have been a religious place
    long ago. You can almost feel the ancient spirits.
    A short path to the 'south' leads to the castle entrance. You also can go 'west' to the forest
    junction, or 'east' to a resting place.
    Don't bother checking, nothing interesting to take.
    """,
    [],
    [],
    False,
    [],
    [],
]
resting_place = [
    6,
    "A peaceful resting place",
    """
    You enter a small clearing. It's so peaceful here! You take a moment to rest on one of
    the benches and clear your mind. After a while, you feel ready to move on.
    The path to the 'west' will take you the eastern forest ruins, while the one 
    to the 'east' surely leads to the deep forest in the east.
    No items here.
    """,
    [],
    [],
    False,
    [],
    [],
]
big_rock = [
    7,
    "Big rock",
    """
    You are deep in the forest to the east. There is a large rock as if a giant has thrown it
    hastily. Among the boulders, you can see a chest.
    To the 'north' a long path will bring you all around to the northern forest entrance.
    The calm resting place is located to the 'west', and also you can see a long path along
    the castle walls to the main entrance to the 'south'.
    """,
    ["There is a 'shield' in the chest", "The chest is empty"],
    [],
    False,
    [],
    ["shield"],
]
main_entrance = [
    8,
    "Main castle entrance",
    """
    You are at the castle entrance. The building is huge, commanding the surrounding area.
    Surely some great treasure lies within!
    The path to the 'north' leads to the forest resting area. To the 'west' you can 
    walk near the castle walls deep back to the forest as well as to the 'east'.
    There is a huge door to the 'south'. You see a statue of a paladin guarding the door.
    While there is a lot of junk here, nothing worth taking.
    """,
    [],
    ['sword', 'shield'],
    True,
    ["The left hand of the statue is empty.", "The right hand of the statue is empty."],
    [],
]
main_hall = [
    9,
    "Main hall",
    """
    You stand in the main hall of the castle. This place is huge! Nothing particularly
    interesting here, though. You can stay admiring the broken furniture or you
    can go to 'north' to the woods, or take the short passage to the 'south'.
    Nothing to take here.
    """,
    [],
    [],
    False,
    [],
    [],
]
castle_junction = [
    10,
    "Castle junction",
    """
    You stand in dark room. The sun barely lights up this place through the broken windows.
    It seem like a junction. You see signs on the corridors. The one to the 'west' reads catacombs,
    the one to the 'east' says temple. There is one to the 'north' saying Main hall, and there
    isn't one to the 'south' one.
    No useful items to be found.
    """,
    [],
    [],
    False,
    [],
    [],
]
catacombs_main = [
    11,
    "Catacombs main hall",
    """
    You can barely see in this large room. There are stairs going down deep in the castle.
    In the twilight, you can see some stairs going down to the 'south' and a corridor leading to
    the juction area to the 'east'.
    """,
    [],
    [],
    False,
    [],
    [],
]
catacombs_rest = [
    12,
    "Catacombs stairs - resting",
    """
    You climbed so many stairs in the dark, you can't even count! You need to sit down and rest for
    a moment. The area is empty, dark and the stones are wet. After a while, you take your courage
    and go further.
    There are stairs leading up to the 'north' and stairs going down to the 'west'.
    No items to take here.
    """,
    [],
    [],
    False,
    [],
    [],
]
catacombs_middle = [
    13,
    "Catacombs middle section",
    """
    This long, empty hallway seems to be the middle point between the catacombs area and the 
    rest of the castle. How many rooms till you find something?
    There are two ways from here, the 'north' one leads further into the catacombs,
    and the 'south' one takes you back, where you rested.
    No items here.
    """,
    [],
    [],
    False,
    [],
    [],
]
catacombs_entrance = [
    14,
    "Catacombs entrance",
    """
    You stand in the entrance of the catacombs. There is an unusual calmness here. You think
    for a second, how big the owner dinasty should have been. Have the buried all the 
    important people here?
    If you go to the 'west', you should enter the burial area. If you take the stairs to the
    'south' a long climb awaits you back to the juction.
    No items here.
    """,
    [],
    [],
    False,
    [],
    [],
]
catacombs_tombs = [
    15,
    "Catacombs Tombs",
    """
    You see tombs everywhere. All of them are covered with writings and ancient, religious
    symbols. The air is wet and cold, you can see your breath. One of the tombs is open.
    There is a skeleton lying in his beds for all eternity, covered in jewels and a crown on
    his head.
    You can only go back to the 'north'.
    """,
    ["The skeleton is holding a 'scepter'", "You are not interested in taking the jewels."],
    [],
    False,
    [],
    ["scepter"],
]
temple_hallway = [
    16,
    "Temple hallway",
    """
    You are standing in a large hallway. The walls are covered with murals. The basins
    for holy water have long been dried up. 
    The corridors can lead you 'north' or 'south' to the norhtern and southern wings, or you can 
    go 'west' to the castle junction area.
    You can't find anything useful.
    """,
    [],
    [],
    False,
    [],
    [],
]
northern_wing = [
    17,
    "Northern wing",
    """
    This is the northern wing to the temple area. It is not as impressively decorated as the
    main hallway, but it is still very nice. You wonder, how many people was attending to 
    worshipping.
    There is a path to the 'south' to the temple hallway, or you can go 'east' along a long
    corridor to the sanctuary.
    Nothing useful here.
    """,
    [],
    [],
    False,
    [],
    [],
]
south_wing = [
    18,
    "South wing",
    """
    This place already collapsed, the floor is covered with rocks and there is a huge hole on
    the ceiling. What the hell happened here?
    The corridor to the 'north' leads you the temple hallway, while the one to the 'east' should
    lead you to the sanctuary.
    You could take the rubble, but decide not to as it is too heavy.
    """,
    [],
    [],
    False,
    [],
    [],
]
sanctuary = [
    19,
    "Sanctuary",
    """
    As you enter, you feel so peacful. The room is almost empty, but there is a statue of a beutiful woman in the middle.
    You wonder, if she is a representation of a godess.
    Two exits are in this room. The 'north' one will lead you to the northern wing, while the 'west' one brings you to the southern wing.
    """,
    ["You see an 'amulet' around the neck of the statue", "Nothing to find here."],
    ["items to use"],
    False,
    [],
    ["amulet"],
]
exit_passage = [
    20,
    "Exit passage",
    """
    You enter in a room, and you can feel the castle exit is near. The room is empty, you can only stare at the bare rocks in the castle wall.
    You can go 'north' to the castle junction, or to the 'south' which leads you to a small alcove, or you can try the long corridor to the 'west'
    """,
    [],
    [],
    False,
    [],
    [],
]
alcove = [
    21,
    "Alcove",
    """
    You stand in a small alcove. There are some tiny windows here, and the sun shines through and lights up two piedestals.
    There is only one exit here to the 'north' which leads you back to the exit passage.
    """,
    [],
    ["amulet", "scepter"],
    False,
    ["There is small opening on the left piedestal, maybe some jewelry can fit in here", "The right piedestal has a narrow opening."],
    [],
]
castle_exit = [
    22,
    "Castle exit",
    """
    You are in the final room! You feel excited, you almost done it. There is a large door blocking your way, it surely leads to outside.
    You can try the door to the 'south' or go 'north' to the exit passage.
    """,
    [],
    [],
    True,
    [],
    [],
]
victory = [
    23,
    "Victory!",
    """
    -------------------------------------------------------
    
    You did it! You wandered around, found some items and used them at the proper place. No treasures, though, which makes you feel sad.
    Maybe next time...
    
    -------------------------------------------------------
    """,
    [],
    [],
    False,
    [],
    [],
]

# ------------------------------------
# ---Adjacency list with the exits ---
#-------------------------------------
# Using the IDs from the location list
adjacency_list = {
    1:  [(forest_junction, 'south'), (big_rock, 'east')],
    2:  [(forest_start, 'north'), (western_ruins, 'west'), (eastern_ruins, 'east')],
    3:  [(forest_junction, 'east'), (west_forest, 'west')],
    4:  [(western_ruins, 'east'), (main_entrance, 'south')],
    5:  [(forest_junction, 'west'), (main_entrance, 'south'), (resting_place, 'east')],
    6:  [(eastern_ruins, 'west'), (big_rock, 'east')],
    7:  [(forest_start, 'north'), (resting_place, 'west'), (main_entrance, 'south')],
    8:  [(eastern_ruins, 'north'), (big_rock, 'east'), (west_forest, 'west'), (main_hall, 'south')],
    9:  [(main_entrance, 'north'), (castle_junction, 'south')],
    10: [(main_hall, 'north'), (temple_hallway, 'east'), (exit_passage, 'south'), (catacombs_main, 'west')],
    11: [(castle_junction, 'east'), (catacombs_rest, 'south')],
    12: [(catacombs_main, 'north'), (catacombs_middle, 'west')],
    13: [(catacombs_rest, 'south'), (catacombs_entrance, 'north')],
    14: [(catacombs_middle, 'south'), (catacombs_tombs, 'west')],
    15: [(catacombs_entrance, 'north')],
    16: [(castle_junction, 'west'), (northern_wing, 'north'), (south_wing, 'south')],
    17: [(temple_hallway, 'south'), (sanctuary, 'east')],
    18: [(temple_hallway, 'north'), (sanctuary, 'east')],                                                         
    19: [(northern_wing, 'north'), (south_wing, 'west')],
    20: [(castle_exit, 'west'), (alcove, 'south'), (castle_junction, 'north')],
    21: [(exit_passage, 'north')],
    22: [(exit_passage, 'north'), (victory, 'south')],
    23: [(castle_exit, )],
}

# Set starting values, inventory empty and starting area as forest start.      
inventory = []
current_location = forest_start
valid_directions = ["north", "south", "east", "west"]
     
        
if __name__ == "__main__":
    # Welcome message
    print()
    print("-" * 28)
    print("---------- CASTLE ----------")
    print("---- L A B I R I N T H -----")
    print("-" * 28)
    print()
    print("Welcome to CASTLE LABIRINTH!")
    print("Navigate through the maze, find and use items to enter the castle and escape!")
    # Display instructions
    get_help()
    
    print("GOOD LUCK!")
    print()
    print("--------------------------------------------------------------")
    print()
       
    #initializing pygame
    
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Castle Labirinth MAP")
    clock = pygame.time.Clock()
    
    # loading the map (the picture is defaulted to the same directory as labirinth.py)
    map_surface = pygame.image.load(".\Labirinth_map_600x600.png")
    
    while True:
        # defining an event loop, only used to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        # display the map with the blit method
        screen.blit(map_surface, (0, 0))
        pygame.display.update()
        
        # main game loop
        
        # printing the name and description of the current location.
        
        print(current_location[1])
        print()
        print(current_location[2])
        print()
        # Check if the items to found list is exists, if yes, display the first element.
        if current_location[3]:
            print(current_location[3][0])
            print()
        # Check if the item using hints exits (last element of the list), if yes, display.
        if current_location[6]:
            for element in current_location[6]:
                print(element)
        
        print('----------')
        print()
        
        # Here we check if we are at the victory location. If so, quit.
        if current_location == victory:
            break
        
        command = input("What to do? Go somewhere or check something: ").lower()

        
        # checking valid commands, like quit, inventory, help, directions, etc.        
        if command == ('quit'):
            pygame.quit()
            exit()
            
        # checking if an item was picked up
        # western ruins
        elif command == 'take sword' and current_location == western_ruins and current_location[7][0] == 'sword':
            inventory.append("sword")
            current_location[7] = ['']
            current_location[3].remove(current_location[3][0])
            western_ruins = current_location        
        # big_rock
        elif command == 'take shield' and current_location == big_rock and current_location[7][0] == 'shield':
            inventory.append("shield")
            current_location[7] = ['']
            current_location[3].remove(current_location[3][0])
            big_rock = current_location
        # catacombs tombs
        elif command == 'take scepter' and current_location == catacombs_tombs and current_location[7][0] == 'scepter':
            inventory.append("scepter")
            current_location[7] = ['']
            current_location[3].remove(current_location[3][0])
            western_ruins = current_location
        # sanctuary
        elif command == 'take amulet' and current_location == sanctuary and current_location[7][0] == 'amulet':
            inventory.append("amulet")
            current_location[7] = ['']
            current_location[3].remove(current_location[3][0])
            western_ruins = current_location    
         
        # checking the inventory    
        elif command == ('inventory'):
            if not inventory:
                print()
                print('You have no items.')
                print()
            else:
                print()
                print('You have:')
                print()
                for item in inventory:
                    print(item)
        elif command == 'help':
            get_help()
             
        # using items, at the main entrance and at the alcove. At both places two items must be used to open the door.
        
        # Main entrance, will open the door at this location if both items are used.
        elif command == 'use sword' and current_location == main_entrance and "sword" in inventory:
            inventory.remove('sword')
            current_location[4][0] = ''
            current_location[6][1] = ''
            main_entrance = current_location
            if main_entrance[4][0] == '' and main_entrance[4][1] == '':
                print("You hear a click and the door opens.")
                main_entrance[5] = False
                current_location = main_entrance
        elif command == 'use shield' and current_location == main_entrance and "shield" in inventory:
            inventory.remove('shield')
            current_location[4][1] = ''
            current_location[6][0] = ''
            main_entrance = current_location
            if main_entrance[4][0] == '' and main_entrance[4][1] == '':
                print("You hear a click and the door opens.")
                main_entrance[5] = False
                current_location = main_entrance
                
        # Alcove, using both items here will open the exit.
        elif command == 'use scepter' and current_location == alcove and "scepter" in inventory:
            inventory.remove('scepter')
            current_location[4][1] = ''
            current_location[6][1] = ''
            alcove = current_location
            if alcove[4][0] == '' and alcove[4][1] == '':
                print("Nearby a door opened.")
                castle_exit[5] = False
        elif command == 'use amulet' and current_location == alcove and "amulet" in inventory:
            inventory.remove('amulet')
            current_location[4][0] = ''
            current_location[6][0] = ''
            alcove = current_location
            if alcove[4][0] == '' and alcove[4][1] == '':
                print("Nearby a door opened.")
                castle_exit[5] = False     
        
        # Navigation logic, checks if the door is closed
        elif command in valid_directions:
            print()
            # access to the list of tuples in the adjacency list for the current location for possible exits
            exits_list = adjacency_list[current_location[0]]
            # iterating over the elements and unpack the tuples, and check if we go to an allowed location
            for element in exits_list:
                target_location, direction = element
                
                if (direction == command and current_location[5] == False) or (direction == command and current_location[5] == True and command != 'south'):
                    print(current_location[5])
                    current_location = target_location
      
        else:
            print()
            print("I don't understand. Invalid command or typo?")
        
        
        
    
    
           
        
       
        
    
    
    

    
  


