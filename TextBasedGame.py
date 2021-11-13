# Martin Salas
# Project Two
# The code is a text based game, gives you instructions and commands to input
# Will output text based on the players input


# function that will output the instructions of the game
def instructions():
    print('Collect 6 magic items to win the game, or die be the hands of the devil.')
    print("Move commands: 'Go North', 'Go East', 'Go South', 'Go West'")
    print('Add to Inventory: Get \'item name\'')
    print('To see the instructions: \'Guide\'')


# function will display to player their location in the game and possible item in room
def show_status(current_room, inventory, rooms):
    location = f'\nYou are in town {current_room}' if current_room != 'Capital' else f'\nYou are in the {current_room}'
    print(location)
    print(f'Inventory : {inventory}')
    if 'Item' in rooms[current_room]:
        print(f'You see a {rooms[current_room].get("Item")}')
        print('-'*25)
        return True
    print('-'*25)
    return False


# function calls the instructions function to show instructions to player
def guide():
    print()
    print('%'*72)
    instructions()
    print('%'*72)


# function will be called when player has lost the game
def you_lose():
    print()
    print('*'*30)
    print('\n          GAME OVER')
    print('You were killed by the devil!\n')
    print('*'*30)
    print()


# function will be called when player has won the game
def you_win():
    print()
    print('*'*56)
    print('\n                     !!!YOU WON!!!')
    print('You defeated the devil and brought peace to the kingdom.\n')
    print('*'*56)
    print()


# function to add item to players inventory
def get_item(current_room, inventory, rooms, item):
    inventory.append(item)
    rooms[current_room].pop('Item')
    print(f'{item} retrieved!')


# function to get players input/move/command
def move_input():
    move = input('Enter your move:\n').title().split()
    return move


# function where the game is taking place
def __main__():
    # Here we have different variables to hold
    current_room = 'Capital'
    inventory = []
    directions = ['North', 'South', 'East', 'West']
    commands = ['Go', 'Get']
    rooms = {
        'Capital': {'North': 'Austin', 'South': 'Plano', 'East': 'Dallas', 'West': 'Houston'},
        'Austin': {'South': 'Capital', 'Item': 'Hat'},
        'Houston': {'East': 'Capital', 'Item': 'Ring'},
        'Dallas': {'West': 'Capital', 'Item': 'Robe'},
        'Plano': {'North': 'Capital', 'West': 'Frisco', 'East': 'Oak', 'Item': 'Necklace'},
        'Frisco': {'East': 'Plano', 'Item': 'Book'},
        'Oak': {'West': 'Plano', 'South': 'Cave', 'Item': 'Staff'},
        'Cave': {'North': 'Oak', 'Item': 'Devil'}
    }

    # THE START OF THE GAME
    print('Wizard Text Based Game\n')
    instructions()
    show_status(current_room, inventory, rooms)
    move = move_input()
    item_present = False

    # while loop to keep the game going till player reach the 'Cave' room
    while current_room != 'Cave':
        # if block to check if player asked for the guide of the game
        if move[0] == 'Guide':
            guide()
            show_status(current_room, inventory, rooms)
            move = move_input()
        # if block to validate players move/command
        elif len(move) <= 1 or move[0] not in commands:
            print('Invalid Input!!!')
            show_status(current_room, inventory, rooms)
            move = move_input()
        # if block will run if players input has 'go'
        elif move[0] == 'Go':
            # if block to check input 'room' is in rooms dictionary
            if move[1] in rooms[current_room]:
                current_room = rooms[current_room].get(move[1])
                item_present = show_status(current_room, inventory, rooms)
                # if block will break from loop if player reach the 'Cave'
                if current_room == 'Cave':
                    break
            # if block will validate players input
            elif move[1] in directions:
                print('You can\'t go that way!')
                show_status(current_room, inventory, rooms)
            else:
                print('Invalid Input!')
                show_status(current_room, inventory, rooms)
            move = move_input()
        # if block will run if player inputted 'get'
        elif move[0] == 'Get':
            # if blocks will run based if there is an item, if so will add to inventory
            if move[1] in rooms[current_room].values():
                get_item(current_room, inventory, rooms, move[1])
                item_present = False
            elif not item_present:
                print('There is no item here!')
            else:
                print('Invalid Input!')
            show_status(current_room, inventory, rooms)
            move = move_input()

    # if loop to check if inventory is less than 6 item
    if len(inventory) < 6:
        you_lose()
    else:
        you_win()


__main__()
