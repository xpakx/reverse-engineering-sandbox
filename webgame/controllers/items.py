from extractors.lib import getStatAsInt
from repo.userdata import GameRepository
from repo.item import ItemDef

userStamina = 0

def buyStamina(request, repo: GameRepository, gameData):
    print(request)
    return {'stamina': 120}


def useStaminaItem(request, repo: GameRepository, gameData):
    print(request)
    itemId = getStatAsInt(request['args'], 'libId')
    amount = getStatAsInt(request['args'], 'amount')
    item = ItemDef(itemId=itemId,
                   itemCount=amount,
                   itemType='consumable')

    inventory = repo.getInventoryByUserId(1)
    enoughResources = inventory.removeItem(item)
    if enoughResources:
        # TODO
        global userStamina
        userStamina += 120
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
