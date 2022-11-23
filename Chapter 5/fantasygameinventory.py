inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory:')
    total_items = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total_items += v
    print('Total number of items: ' + str(total_items) + '\n')

displayInventory(inventory)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(inv)
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)