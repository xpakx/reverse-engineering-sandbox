from extractors.lib import Hero
from repo.hero import getTestHeroes, applyHeroes
from repo.shop import getTestShops, Shop
from typing import List
from repo.item import Inventory
from repo.shop import ItemDef


class GameRepository:
    def __init__(self, gameData):
        self.gameData = gameData
        self.inventoryById = {}
        self.heroesById = {}
        self.shopsById = {}
        self.staminaById = {}
        self.tempUser = None

    def getInventoryByUserId(self, id: int) -> Inventory:
        if id in self.inventoryById:
            return self.inventoryById[id]
        newInventory = getTestInventory()
        self.inventoryById[id] = newInventory
        return newInventory

    def getHeroesByUserId(self, id: int) -> List[Hero]:
        if id in self.heroesById:
            return self.heroesById[id]
        newHeroes = applyHeroes(getTestHeroes(), self.gameData)
        self.heroesById[id] = newHeroes
        return newHeroes

    def getShopsByUserId(self, id: int) -> List[Shop]:
        if id in self.shopsById:
            return self.shopsById[id]
        newShops = getTestShops()
        self.shopsById[id] = newShops
        return newShops

    def getStaminaMyUserId(self, id: int) -> int:
        if id in self.staminaById:
            return self.staminaById[id]
        self.staminaById[id] = 120
        return 120

    def setStaminaMyUserId(self, id: int, value: int):
        self.staminaById[id] = value


it = {
        'bottledEnergy': 17,
        'bigExp': 11,
    }


def getTestInventory():
    inv = Inventory(1)
    inv.gold = 500000
    inv.emeralds = 500000
    inv.addItem(
                ItemDef(
                    itemType='consumable',
                    itemId=it['bigExp'],
                    itemCount=20))
    inv.addItem(
                ItemDef(
                    itemType='consumable',
                    itemId=it['bottledEnergy'],
                    itemCount=30))
    return inv
