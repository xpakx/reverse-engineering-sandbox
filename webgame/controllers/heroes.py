from typing import NamedTuple
import json

userHeroes = [3]
attrs = ["strength", "physicalCritChance", "physicalAttack",
         "magicResist", "magicPower", "magicPenetration",
         "lifesteal", "intelligence", "hp",
         "dodge", "armorPenetration", "armor",
         "agility"]


def getHeroById(id):
    return {
            "id": id,
            "xp": 300105,
            "level": 68,
            "color": 9,
            "slots": [0, 0, 0],
            "skills": {
                "432": 67,
                "433": 67,
                "434": 67,
                "435": 67
                },
            "power": 19156,
            "star": 3,
            "runes": [3230, 0, 100, 2790, 0],
            "skins": {"3": 48},
            "currentSkin": 3,
            "titanGiftLevel": 14,
            "titanCoinsSpent": {
                "consumable": {"24": 12110}
                },
            "artifacts": [
                {"level": 6, "star": 2},
                {"level": 23, "star": 4},
                {"level": 19, "star": 1}
                ],
            "scale": 1,
            "petId": 0,
            "type": "hero",
            "perks": [6, 1],
            "ascensions": {"1": [0, 1, 2, 3]}
        }


def getUserHeroes(request, temp, gameData):
    result = {}
    for id in userHeroes:
        result[str(id)] = getHeroById(id)
    return result


class StatData(NamedTuple):
    strength: int = 0
    physicalCritChance: int = 0
    physicalAttack: int = 0
    magicResist: int = 0
    magicPower: int = 0
    magicPenetration: int = 0
    lifesteal: int = 0
    intelligence: int = 0
    hp: int = 0
    dodge: int = 0
    armorPenetration: int = 0
    armor: int = 0
    agility: int = 0


heroBaseData = {
    3: StatData(intelligence=15, agility=20, strength=10, hp=500, physicalAttack=60),
    }

mainStat = {
        3: "agility",
    }

heroStarData = {
        3: [
            StatData(intelligence=3, agility=4, strength=3),
            StatData(intelligence=3, agility=7, strength=5),
            StatData(intelligence=5, agility=10, strength=7),
            StatData(intelligence=7, agility=15, strength=8),
            StatData(intelligence=9, agility=20, strength=11),
            StatData(intelligence=11, agility=24, strength=15),
        ],
    }


class Hero:
    def __init__(self, id: int):
        base = heroBaseData[id]
        self.strength = base.strength
        self.physicalCritChance = base.physicalCritChance
        self.physicalAttack = base.physicalAttack
        self.magicResist = base.magicResist
        self.magicPower = base.magicPower
        self.magicPenetration = base.magicPenetration
        self.lifesteal = base.lifesteal
        self.intelligence = base.intelligence
        self.hp = base.hp
        self.dodge = base.dodge
        self.armorPenetration = base.armorPenetration
        self.armor = base.armor
        self.agility = base.agility
        self.mainStat = mainStat[id]
        self.id = id

    def processBaseStats(self):
        self.physicalAttack = self.physicalAttack + 2 * self.agility + self.getMainAttr()
        self.hp = self.hp + 40 * self.strength
        self.armor = self.armor + self.agility
        self.magicPower = self.magicPower + 3 * self.intelligence
        self.magicResist = self.magicResist + self.intelligence

    def getMainAttr(self):
        if not hasattr(self, self.mainStat):
            return 0
        return getattr(self, self.mainStat)

    def update(self, stat: StatData, times: int = 1):
        for attr in attrs:
            if not hasattr(self, attr) or not hasattr(stat, attr):
                continue
            new_value = getattr(self, attr) + getattr(stat, attr) * times
            setattr(self, attr, new_value)

    def applyStarsAndLevel(self, stars: int, level: int):
        starsData = heroStarData[self.id][stars-1]
        self.update(starsData, level)


def getTestHero(id):
    hero = getHeroById(id)
    hero['agility'] = 27
    hero['intelligence'] = 52
    hero['hp'] = 700
    hero['physicalAttack'] = 50
    hero['strength'] = 32
    hero['armor'] = 25
    hero['magicPower'] = 25
    hero['magicResist'] = 25
    hero['skin'] = 0
    hero['favorPetId'] = 0
    hero['favorPower'] = 0
    return hero


def testHeroData(id: int, level: int, stars: int):
    hero = Hero(id)
    hero.applyStarsAndLevel(stars, level)
    hero.processBaseStats()
    resp = {}
    for attr in attrs:
        value = getattr(hero, attr)
        resp[attr] = value
    response = json.dumps(resp)
    return response
