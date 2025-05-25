from extractors.lib import getStatAsInt, GameData
from controllers.items import addMultToInventory, removeFromInventory
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
        return []

    cost = shop.slots[slot-1].cost
    enoughResources = removeFromInventory(repo, cost.itemType, cost.itemId, cost.itemCount)
    if not enoughResources:
        # error
        return []
    shop.slots[slot-1].bought = True
    shopResponse = shop.toResponse()
    reward = shopResponse['slots'][str(slot)]['reward']
    addMultToInventory(repo, reward)
    return []
