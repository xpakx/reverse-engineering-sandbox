from typing import NamedTuple, List, Any, Dict
from datetime import datetime, timedelta


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
        self.id: int = id
        self.slots: List[ShopSlot] = []
        self.updateRefreshTime()

    def updateRefreshTime(self):
        today = datetime.now()
        todayNoon = datetime(today.year, today.month, today.day, 12, 0, 0)
        if today >= todayNoon:
            noonTime = todayNoon + timedelta(days=1)
        else:
            noonTime = todayNoon
        self.refreshAt = int(noonTime.timestamp())

    def toResponse(self):
        shop = {}
        shop['id'] = self.id
        shop['availableUntil'] = 0
        shop['refreshTime'] = self.refreshAt
        shop['slots'] = {}
        shop['level'] = 0
        for i in range(len(self.slots)):
            slot = self.slots[i]
            addItem(shop['slots'], i, slot.item, slot.cost, slot.bought)
        return shop


def addItem(
        slots: Dict[str, Any],
        slotNum: int,
        item: ItemDef,
        cost: ItemDef,
        bought: bool = False):
    slot = {}
    slots[str(slotNum)] = slot
    slot['id'] = slotNum
    slot['reward'] = item.toResponse()
    slot['bought'] = 1 if bought else 0
    slot['cost'] = cost.toResponse()
    slot['pinned'] = False
    slot['amountAvailable'] = None


def getTestShops():
    result = {}
    result[1] = getTownShop()
    result[4] = getArenaShop()
    result[5] = getGrandArenaShop()
    result[6] = getTowerShop()
    result[8] = getSoulShop()
    result[9] = getFriendshipShop()
    return result


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
