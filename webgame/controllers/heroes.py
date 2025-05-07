from extractors.lib import GameData, Hero, getStatAsInt
from typing import List, NamedTuple, Optional


def getHeroById(id: int, data: GameData):
    heroData = data.heroes[id]
    hero = Hero(heroData)
    hero.applyStarsAndLevel(3, 68)
    hero.applyColor(9)
    return hero.getProfileData()


def getUserHeroes(request, temp, gameData: GameData):
    result = {}
    userHeroes = temp['heroes']
    for hero in userHeroes:
        result[str(hero.data.id)] = hero.getProfileData()
    return result


class UserHero(NamedTuple):
    id: int = 0
    stars: int = 1
    level: int = 1
    color: int = 1


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
        hero.skills[0] = 1
        result.append(hero)
    return result


def upgradeSkill(request, temp, gameData: GameData):
    heroId = getStatAsInt(request['args'], 'heroId')
    skillNum = getStatAsInt(request['args'], 'skill') - 1
    hero: Optional[Hero] = None
    for h in temp['heroes']:
        if h.data.id == heroId:
            hero = h
            break
    if not hero:
        return None
    hero.skills[skillNum] += 1
    return None


def evolveHero(request, temp, gameData: GameData):
    heroId = getStatAsInt(request['args'], 'heroId')
    # TODO: errors, verify and deduct gold

    userHeroes = temp['heroes']
    for hero in userHeroes:
        if hero.data.id == heroId:
            hero.stars += 1
    return []


def addExpToHero(request, temp, gameData: GameData):
    heroId = getStatAsInt(request['args'], 'heroId')
    # consumableId = getStatAsInt(request['args'], 'libId')
    consumableAmount = getStatAsInt(request['args'], 'amount')
    exp = 1500 * consumableAmount
    userHeroes: List[Hero] = temp['heroes']
    for hero in userHeroes:
        if hero.data.id == heroId:
            hero.addExperience(exp, gameData.levelToExp)
    return []


def getHeroRatings(request, temp, gameData: GameData):
    response = {}
    response['userRating'] = []
    response['rating'] = {}
    for i in range(1, 67):
        response['rating'][str(i)] = 4.00
    return response
