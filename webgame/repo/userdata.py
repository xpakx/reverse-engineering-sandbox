from extractors.lib import Hero
from controllers.items import getTestInventory
from controllers.heroes import getTestHeroes, applyHeroes
from controllers.shop import getTestShops, Shop
from typing import Dict, Any, List


class GameRepository:
    def __init__(self, gameData):
        self.gameData = gameData
        self.inventoryById = {}
        self.heroesById = {}
        self.shopsById = {}

    def getInventoryByUserId(self, id: int) -> Dict[str, Any]:
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
