from typing import NamedTuple, List
from extractors.lib import getStatAsInt
from controllers.items import addMultToInventory


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


class ShopSlot:
    item: ItemDef
    cost: ItemDef
    bought: bool

    def __init__(
            self,
            item: ItemDef = ItemDef(),
            cost: ItemDef = ItemDef(),
            bought: bool = False):
        self.item = item
        self.cost = cost
        self.bought = bought


class Shop:
    def __init__(self, id: int):
        self.id = id
        self.slots = []

    def toResponse(self):
        shop = {}
        shop['id'] = self.id
        shop['availableUntil'] = 0
        shop['refreshTime'] = 1745564400
        shop['slots'] = {}
        for i in range(len(self.slots)):
            slot = self.slots[i]
            addItem(shop['slots'], i, slot.item, slot.cost, slot.bought)
        return shop


def getShops(request, temp, gameData):
    response = {}
    shops = [1, 4, 5, 6, 8, 9]
    for shopId in shops:
        response[str(shopId)] = getShopResponseById(temp, shopId)
    return response


def getTestShops():
    result = {}
    result[1] = getTownShop()
    result[4] = getArenaShop()
    result[5] = getGrandArenaShop()
    result[6] = getTowerShop()
    result[8] = getSoulShop()
    result[9] = getFriendshipShop()
    return result


def getShopResponseById(temp, id):
    return temp['shops'][id].toResponse()


def getShopById(temp, id):
    return temp['shops'][id]


def addItem(slots, slotNum, item: ItemDef, cost: ItemDef, bought: bool = False):
    slot = {}
    slots[str(slotNum)] = slot
    slot['id'] = str(slotNum)
    slot['reward'] = item.toResponse()
    slot['bought'] = 1 if bought else 0
    slot['cost'] = cost.toResponse()


def getTownShop():
    shop = Shop(1)
    shop.slots.append(
            ShopSlot(
                ItemDef(itemType='consumable', itemId=11, itemCount=500),
                ItemDef(itemType='gold', itemCount=1),
                )
            )
    shop.slots.append(
            ShopSlot(
                ItemDef(itemType='fragmentHero', itemId=67, itemCount=500),
                ItemDef(itemType='gold', itemCount=1),
                )
            )
    shop.slots.append(
            ShopSlot(
                ItemDef(itemType='fragmentHero', itemId=3, itemCount=500),
                ItemDef(itemType='gold', itemCount=1),
                )
            )
    shop.slots.append(
            ShopSlot(
                ItemDef(itemType='fragmentHero', itemId=50, itemCount=500),
                ItemDef(itemType='gold', itemCount=1),
                )
            )
    shop.slots.append(
            ShopSlot(
                ItemDef(itemType='fragmentHero', itemId=51, itemCount=500),
                ItemDef(itemType='gold', itemCount=1),
                )
            )
    return shop


def getArenaShop():
    shop = Shop(4)
    shop.slots.append(
            ShopSlot(
                ItemDef(itemType='fragmentHero', itemId=19, itemCount=5),
                ItemDef(itemType='coin', itemId=1, itemCount=500),
                )
            )
    return shop


def getGrandArenaShop():
    shop = Shop(5)
    shop.slots.append(
            ShopSlot(
                ItemDef(itemType='fragmentHero', itemId=23, itemCount=5),
                ItemDef(itemType='coin', itemId=2, itemCount=500),
                )
            )
    return shop


def getTowerShop():
    shop = Shop(6)
    shop.slots.append(
            ShopSlot(
                ItemDef(itemType='fragmentHero', itemId=5, itemCount=5),
                ItemDef(itemType='coin', itemId=3, itemCount=500),
                )
            )
    return shop


def getSoulShop():
    shop = Shop(8)
    shop.slots.append(
            ShopSlot(
                ItemDef(itemType='fragmentHero', itemId=31, itemCount=5),
                ItemDef(itemType='coin', itemId=5, itemCount=500),
                )
            )
    return shop


def getFriendshipShop():
    shop = Shop(9)
    shop.slots.append(
            ShopSlot(
                ItemDef(itemType='fragmentHero', itemId=10, itemCount=5),
                ItemDef(itemType='coin', itemId=6, itemCount=500),
                )
            )
    return shop


def buy(request, temp, gameData):
    shopId = getStatAsInt(request['args'], 'shopId')
    shop = getShopById(temp, shopId)
    slot = getStatAsInt(request['args'], 'slot')
    if shop.slots[slot-1].bought:
        # error
        return []
    shop.slots[slot-1].bought = True
    shopResponse = shop.toResponse()
    reward = shopResponse['slots'][str(slot)]['reward']
    addMultToInventory(temp, reward)
    return []
