from typing import List, NamedTuple
from extractors.lib import GameData, Hero


class UserHero(NamedTuple):
    id: int = 0
    stars: int = 1
    level: int = 1
    color: int = 1
    gear: List[bool] = []


def getTestHeroes() -> List[UserHero]:
    return [
            UserHero(id=3, level=1),
            UserHero(id=4, level=1, stars=2),
            UserHero(id=67, level=1, stars=2),
        ]


def applyHeroes(userData: List[UserHero], data: GameData):
    result = []
    for userHero in userData:
        heroData = data.heroes[userHero.id]
        hero = Hero(heroData)
        hero.applyStarsAndLevel(userHero.stars, userHero.level)
        hero.applyColor(userHero.color)
        hero.applyGear(userHero.gear)
        hero.skills[0] = 1
        result.append(hero)
    return result
