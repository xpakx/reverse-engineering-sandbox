from extractors.lib import getStatAsInt
from repo.userdata import GameRepository
from repo.item import ItemDef


def buyStamina(request, repo: GameRepository, gameData):
    print(request)
    return {'stamina': 120}


def useStaminaItem(request, repo: GameRepository, gameData):
    print(request)
    itemId = getStatAsInt(request['args'], 'libId')
    amount = getStatAsInt(request['args'], 'amount')
    return []


def inventory(request, repo: GameRepository, gameData):
    return repo.getInventoryByUserId(1)


def addToInventory(repo: GameRepository, category: str, id: int, amount: int):
    inventory = repo.getInventoryByUserId(1)
    if category not in inventory:
        inventory[category] = {}

    cat = inventory[category]
    strId = str(id)
    if strId not in cat:
        cat[strId] = 0

    cat[strId] = cat[strId] + amount


def addMultToInventory(repo: GameRepository, reward):
    for category in reward:
        items = reward[category]
        if isinstance(items, dict):
            for item in items:
                id = int(item)
                amount = int(items[item])
                addToInventory(repo, category, id, amount)


def removeFromInventory(repo: GameRepository, item: ItemDef) -> bool:
    if item.itemType == 'gold':
        return True  # TODO

    inventory = repo.getInventoryByUserId(1)
    if item.itemType not in inventory:
        inventory[item.itemType] = {}

    cat = inventory[item.itemType]
    strId = str(item.itemId)
    if strId not in cat:
        cat[strId] = 0

    print(cat[strId])
    if cat[strId] < item.itemCount:
        return False
    cat[strId] = cat[strId] - item.itemCount
    return True
