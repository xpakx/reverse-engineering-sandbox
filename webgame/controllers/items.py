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
    return repo.getInventoryByUserId(1).toResponse()


def addToInventory(repo: GameRepository, category: str, id: int, amount: int):
    inventory = repo.getInventoryByUserId(1)
    item = ItemDef(itemType=category, itemId=id, itemCount=amount)
    inventory.addItem(item)


def addMultToInventory(repo: GameRepository, reward):
    for category in reward:
        items = reward[category]
        if isinstance(items, dict):
            for item in items:
                id = int(item)
                amount = int(items[item])
                addToInventory(repo, category, id, amount)


def removeFromInventory(repo: GameRepository, item: ItemDef) -> bool:
    inventory = repo.getInventoryByUserId(1)
    result = inventory.removeItem(item)
    return result
