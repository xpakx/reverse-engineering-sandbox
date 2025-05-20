from extractors.lib import Hero
from controllers.items import getTestInventory
from controllers.heroes import getTestHeroes, applyHeroes
from controllers.shop import getTestShops, Shop
from typing import Dict, Any, List

inventoryById = {}
heroesById = {}
shopsById = {}


def getInventoryByUserId(id: int) -> Dict[str, Any]:
    if id in inventoryById:
        return inventoryById[id]
    newInventory = getTestInventory()
    inventoryById[id] = newInventory
    return newInventory


def getHeroesByUserId(id: int, gameData) -> List[Hero]:
    if id in heroesById:
        return heroesById[id]
    newHeroes = applyHeroes(getTestHeroes(), gameData)
    heroesById[id] = newHeroes
    return newHeroes


def getShopsByUserId(id: int) -> List[Shop]:
    if id in shopsById:
        return shopsById[id]
    newShops = getTestShops()
    shopsById[id] = newShops
    return newShops
