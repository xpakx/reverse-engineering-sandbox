from extractors.lib import Hero
from controllers.items import getTestInventory
from controllers.heroes import getTestHeroes, applyHeroes
from controllers.shop import getTestShops, Shop
from typing import Dict, Any, List


def getInventoryByUserId(id: int) -> Dict[str, Any]:
    return getTestInventory()


def getHeroesByUserId(id: int, gameData) -> List[Hero]:
    return applyHeroes(getTestHeroes(), gameData)


def getShopsByUserId(id: int) -> List[Shop]:
    return getTestShops()
