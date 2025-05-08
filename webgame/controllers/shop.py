from typing import NamedTuple
from extractors.lib import getStatAsInt
from controllers.items import addMultToInventory


def getShops(request, temp, gameData):
    response = {}
    response['1'] = getShopById(1)
    response['4'] = getShopById(4)
    response['5'] = getShopById(5)
    response['6'] = getShopById(6)
    response['8'] = getShopById(8)
    response['9'] = getShopById(9)
    return response


def getShopById(id):
    if id == 1:
        return getTownShop()
    if id == 4:
        return getArenaShop()
    if id == 5:
        return getGrandArenaShop()
    if id == 6:
        return getTowerShop()
    if id == 8:
        return getFriendshipShop()
    if id == 9:
        return getOutlandShop()


class ItemDef(NamedTuple):
    itemType: str = 'gear'
    itemId: int = 0
    itemCount: int = 1
    ident: str = 'body'

    def toResponse(self):
        if self.itemType in ['gold', 'starmoney']:
            return {self.itemType: str(self.itemCount)}
        return {
                self.itemType: {
                    str(self.itemId): str(self.itemCount)
                    }
                }


def addItem(slots, slotNum, item: ItemDef, cost: ItemDef):
    slot = {}
    slots[str(slotNum)] = slot
    slot['id'] = str(slotNum)
    slot['reward'] = item.toResponse()
    slot['bought'] = 0
    slot['cost'] = cost.toResponse()


def getTownShop():
    shop = {}
    shop['id'] = 1
    shop['availableUntil'] = 0
    shop['refreshTime'] = 1745564400
    shop['slots'] = {}
    addItem(
            shop['slots'],
            1,
            ItemDef(itemType='consumable', itemId=11, itemCount=500),
            ItemDef(itemType='gold', itemCount=1),
            )
    addItem(
            shop['slots'],
            2,
            ItemDef(itemType='fragmentHero', itemId=67, itemCount=500),
            ItemDef(itemType='gold', itemCount=1),
            )
    addItem(
            shop['slots'],
            3,
            ItemDef(itemType='fragmentHero', itemId=3, itemCount=500),
            ItemDef(itemType='gold', itemCount=1),
            )
    addItem(
            shop['slots'],
            4,
            ItemDef(itemType='fragmentHero', itemId=50, itemCount=500),
            ItemDef(itemType='gold', itemCount=1),
            )
    addItem(
            shop['slots'],
            5,
            ItemDef(itemType='fragmentHero', itemId=51, itemCount=500),
            ItemDef(itemType='gold', itemCount=1),
            )
    return shop


def getArenaShop():
    shop = {}
    shop['id'] = 4
    shop['availableUntil'] = 0
    shop['refreshTime'] = 1745564400
    shop['slots'] = {}
    addItem(
            shop['slots'],
            1,
            ItemDef(itemType='fragmentHero', itemId=19, itemCount=5),
            ItemDef(itemType='coin', itemId=1, itemCount=500),
            )
    return shop


def getGrandArenaShop():
    shop = {}
    shop['id'] = 5
    shop['availableUntil'] = 0
    shop['refreshTime'] = 1745564400
    shop['slots'] = {}
    addItem(
            shop['slots'],
            1,
            ItemDef(itemType='fragmentHero', itemId=23, itemCount=5),
            ItemDef(itemType='coin', itemId=2, itemCount=500),
            )
    return shop


def getTowerShop():
    shop = {}
    shop['id'] = 6
    shop['availableUntil'] = 0
    shop['refreshTime'] = 1745564400
    shop['slots'] = {}
    addItem(
            shop['slots'],
            1,
            ItemDef(itemType='fragmentHero', itemId=5, itemCount=5),
            ItemDef(itemType='coin', itemId=3, itemCount=500),
            )
    return shop


def getFriendshipShop():
    shop = {}
    shop['id'] = 8
    shop['availableUntil'] = 0
    shop['refreshTime'] = 1745564400
    shop['slots'] = {}
    addItem(
            shop['slots'],
            1,
            ItemDef(itemType='fragmentHero', itemId=31, itemCount=5),
            ItemDef(itemType='coin', itemId=5, itemCount=500),
            )
    return shop


def getOutlandShop():
    shop = {}
    shop['id'] = 9
    shop['availableUntil'] = 0
    shop['refreshTime'] = 1745564400
    shop['slots'] = {}
    addItem(
            shop['slots'],
            1,
            ItemDef(itemType='fragmentHero', itemId=10, itemCount=5),
            ItemDef(itemType='coin', itemId=6, itemCount=500),
            )
    return shop


def buy(request, temp, gameData):
    shopId = getStatAsInt(request['args'], 'shopId')
    shop = getShopById(shopId)
    slot = getStatAsInt(request['args'], 'slot')
    print(shop['slots'][str(slot)])
    reward = shop['slots'][str(slot)]['reward']
    addMultToInventory(temp, reward)
    return []



