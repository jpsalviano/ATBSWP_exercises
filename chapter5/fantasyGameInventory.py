# Fantasy Game Inventory

bp1 = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}

def displayInventory(backpack):
    print('Inventory:')
    total = 0
    for item, quantity in backpack.items():
        print(str(quantity) + ' ' + item)
        total += quantity
    print('Total number of items: ' + str(total))

displayInventory(bp1)

print('\n' + 'A DRAGON APPEARS!' + '\n')

print('YOU KILLED IT!' + '\n')

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print('Dragon\'s loot: ' + str(dragonLoot))

def addToInventory(backpack, addedItems):
    for item in addedItems:
        if item in backpack:
            backpack[item] += 1
        else:
            backpack.setdefault(item, 1)
    return backpack

addToInventory(bp1, dragonLoot)
print('\n' + 'Inventory updated!' + '\n')
displayInventory(bp1)
