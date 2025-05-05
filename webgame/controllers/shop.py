from typing import NamedTuple


def getShops(request, temp, gameData):
    response = {}
    response['1'] = getTownShop()
    response['4'] = getArenaShop()
    response['5'] = getGrandArenaShop()
    response['6'] = getTowerShop()
    response['8'] = getFriendshipShop()
    response['9'] = getOutlandShop()
    return response


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
            ItemDef(itemType='consumable', itemId=11, itemCount=45),
            ItemDef(itemType='gold', itemCount=450000),
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
