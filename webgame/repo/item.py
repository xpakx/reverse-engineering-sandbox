from typing import NamedTuple, Dict, List


class ItemDef(NamedTuple):
    itemType: str = 'gear'
    itemId: int = 0
    itemCount: int = 1

    def toResponse(self):
        if self.itemType in ['gold', 'starmoney']:
            return {self.itemType: str(self.itemCount)}
        return {
                self.itemType: {
                    str(self.itemId): str(self.itemCount)
                    }
                }


class Inventory:
    def __init__(self, id: int):
        self.gold = 0
        self.emeralds = 0
        self.items: Dict[str, Dict[int, ItemDef]] = {}
        self.items['consumable'] = {}
        self.items['gear'] = {}
        self.items['fragmentHero'] = {}
        self.items['scroll'] = {}
        self.items['coin'] = {}
        self.items['fragmentGear'] = {}
        self.items['fragmentScroll'] = {}
        self.items['fragmentArtifact'] = {}
        self.items['fragmentTitan'] = {}
        self.items['fragmentTitanArtifact'] = {}
        self.items['ascensionGear'] = {}
        self.items['fragmentPet'] = {}
        self.items['petGear'] = {}

    def addItem(self, item: ItemDef):
        if item.itemType == 'gold':
            self.gold = self.gold + item.itemCount
            return
        if item.itemType == 'starmoney':
            self.emeralds = self.emeralds + item.itemCount
            return
        category = self.items[item.itemType]
        if item.itemId not in category:
            category[item.itemId] = item
            return
        invItem = category[item.itemId]
        self.updateCount(item, invItem.itemCount + item.itemCount)

    def addItemMult(self, items: List[ItemDef]):
        for item in items:
            self.addItem(item)

    def removeItem(self, item: ItemDef) -> bool:
        print(item)
        if item.itemType == 'gold':
            if self.gold < item.itemCount:
                return False
            self.gold = self.gold - item.itemCount
            return True
        if item.itemType == 'starmoney':
            if self.emeralds < item.itemCount:
                return False
            self.emeralds = self.emeralds - item.itemCount
            return True

        category = self.items[item.itemType]
        if item.itemId not in category:
            return False

        invItem = category[item.itemId]
        if invItem.itemCount < item.itemCount:
            return False
        self.updateCount(item, invItem.itemCount - item.itemCount)
        return True

    def removeItemUnsafe(self, item: ItemDef):
        if item.itemType == 'gold':
            self.gold = self.gold - item.itemCount
            return
        if item.itemType == 'starmoney':
            self.emeralds = self.emeralds - item.itemCount
            return
        category = self.items[item.itemType]
        if item.itemId not in category:
            return
        invItem = category[item.itemId]
        self.updateCount(item, invItem.itemCount - item.itemCount)

    def checkItem(self, item: ItemDef) -> bool:
        if item.itemType == 'gold':
            return self.gold >= item.itemCount
        if item.itemType == 'starmoney':
            return self.emeralds >= item.itemCount
        category = self.items[item.itemType]
        if item.itemId not in category:
            return False
        invItem = category[item.itemId]
        return invItem.itemCount >= item.itemCount

    def removeItemMult(self, items: List[ItemDef]) -> bool:
        for item in items:
            if not self.checkItem(item):
                return False
        for item in items:
            self.removeItemUnsafe(item)
        return True

    def updateCount(self, item: ItemDef, count: int):
        category = self.items[item.itemType]
        category[item.itemId] = ItemDef(
                itemType=item.itemType,
                itemId=item.itemId,
                itemCount=count
                )

    def toResponse(self):
        response = {}
        for category in self.items:
            cat = {}
            for item in self.items[category]:
                it = self.items[category][item]
                cat[str(it.itemId)] = it.itemCount
            response[category] = cat
        return response
