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
