from extractors.lib import getStatAsInt, GameData
from repo.userdata import GameRepository


def getShops(request, repo: GameRepository, gameData: GameData):
    response = {}
    shops = [1, 4, 5, 6, 8, 9]
    for shopId in shops:
        response[str(shopId)] = getShopResponseById(repo, shopId)
    return response


def getShopResponseById(repo: GameRepository, id: int):
    return repo.getShopsByUserId(1)[id].toResponse()


def getShopById(repo: GameRepository, id: int):
    return repo.getShopsByUserId(1)[id]


def buy(request, repo: GameRepository, gameData: GameData):
    shopId = getStatAsInt(request['args'], 'shopId')
    shop = getShopById(repo, shopId)
    slot = getStatAsInt(request['args'], 'slot')

    if shop.slots[slot-1].bought:
        # error
        print("Shop warning: item already bought")
        return []

    cost = shop.slots[slot-1].cost
    inventory = repo.getInventoryByUserId(1)
    enoughResources = inventory.removeItem(cost)
    if not enoughResources:
        # error
        print("Shop warning: not enough resources")
        return []
    shop.slots[slot-1].bought = True
    reward = shop.slots[slot-1].item
    inventory.addItem(reward)
    return []
