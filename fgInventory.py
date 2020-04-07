def fgInventory():
    '''
    ATBSwP Practice Project: Fantasy Game Inventory
    https://automatetheboringstuff.com/2e/chapter5/

    You are creating a fantasy video game. The data structure to model the
    player’s inventory will be a dictionary where the keys are string values
    describing the item in the inventory and the value is an integer value
    detailing how many of that item the player has. For example, the dictionary
    value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    means the player has 1 rope, 6 torches, 42 gold coins, and so on.
    '''

    inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow':
    12}

    displayInventory(inventory)
    dragonYN = input('\nAre you ready to slay the dragon? ')
    dragonYN = dragonYN.lower()
    if dragonYN[0] == 'n':
        print('Program terminated.')
        exit()
    elif dragonYN[0] == 'y':
        addToInventory(inventory)
        print('\nYou returned alive!')
        displayInventory(inventory)

def displayInventory(inventory):
    itemLength = 0
    itemTotal = 0
    for key, value in inventory.items():
        if itemLength < len(key):
            itemLength = len(key)

    print('\nYour character\'s current inventory:\n')
    for key, value in inventory.items():
        print('\t' + key.ljust(itemLength) + ': ' + str(value))
        itemTotal = itemTotal + value

    print('\n\tTotal number of items: ' + str(itemTotal))

def addToInventory(inventory):
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    for loot in dragonLoot:
        inventory.setdefault(loot, 0)
        inventory[loot] = inventory[loot] + 1

    return inventory

fgInventory()
