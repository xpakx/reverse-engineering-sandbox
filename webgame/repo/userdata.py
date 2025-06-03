from extractors.lib import Hero
from repo.hero import getTestHeroes, applyHeroes
from repo.shop import getTestShops, Shop
from typing import List, Optional
from repo.item import Inventory
from repo.shop import ItemDef
from dataclasses import dataclass


@dataclass
class RefillableData:
    id: int
    amount: id
    lastRefill: int
    boughtToday: bool

    def toResponse(self):
        return {
                "id": self.id,
                "amount": self.amount,
                "lastRefill": self.lastRefill,
                "boughtToday": 1 if self.boughtToday else 0
                }


@dataclass
class UserSummary:
    username: str
    teamLevel: int
    teamExp: int
    vipExp: int


class GameRepository:
    def __init__(self, gameData):
        self.gameData = gameData
        self.inventoryById = {}
        self.heroesById = {}
        self.shopsById = {}
        self.staminaById = {}
        self.usersById = {}
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

    def getHeroByUserIdAndId(self, userId: int, heroId: int) -> Optional[Hero]:
        userHeroes = self.getHeroesByUserId(userId)
        for hero in userHeroes:
            if hero.data.id == heroId:
                return hero
        return None

    def getShopsByUserId(self, id: int) -> List[Shop]:
        if id in self.shopsById:
            return self.shopsById[id]
        newShops = getTestShops()
        self.shopsById[id] = newShops
        return newShops

    def getStaminaByUserId(self, id: int) -> RefillableData:
        if id in self.staminaById:
            return self.staminaById[id]
        self.staminaById[id] = RefillableData(1, 120, 0, False)
        return self.staminaById[id]

    def setStaminaByUserId(self, id: int, value: int):
        self.staminaById[id].amount = value

    def getUserSummary(self, id: int) -> UserSummary:
        if id in self.usersById:
            return self.usersById[id]
        self.usersById[id] = UserSummary(
                "Sir Rocinante",
                68,
                120,
                50000
                )
        return self.usersById[id]


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
    inv.addItem(
                ItemDef(
                    itemType='gear',
                    itemId=8,
                    itemCount=30))
    return inv
